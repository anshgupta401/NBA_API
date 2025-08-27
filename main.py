from io import StringIO, TextIOWrapper
import time
from typing import List
from fastapi import Depends, FastAPI, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from datetime import datetime
import models,schemas,crud
from database import local_session, engine
from helper_functions import get_player_season_stats
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import csv
import pandas as pd
from sqlalchemy import select
from models_all_orm import *
from schemas import PlayerFilter, BasicPlayers

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()

def schedule():
    print("This function has been run")

def read_csv():
    empty_list = []
    with open("test.csv",mode="r") as f:
        data = csv.reader(f)
        for i in data:
            empty_list.append(i)
    db = next(get_db())
    for i in empty_list:
        names = i[0].split()
        player = crud.get_player(db,names[0],names[1])
        if not player:
            new_player = crud.create_player(db,schemas.PlayerCreate(first_name = names[0],last_name = names[1]))
        stats = get_player_season_stats(names[0],names[1],2024)
        if not stats:
            raise HTTPException(status_code=404,detail="Player Stats not Found")
        results = []
        for game in stats:
            try:
                # Convert date string to date object
                game_date = datetime.strptime(game["Date"], "%Y-%m-%d").date()

                # Create stats entry
                stats_data = schemas.PlayerSeasonStatsCreate(
                    date=game_date,
                    team=game.get("Team", ""),
                    opponent=game.get("Opp", ""),
                    location=game.get("Loc", ""),
                    outcome=game.get("Out", ""),
                    minutes_played=game.get("MP", ""),
                    points=int(game.get("PTS", 0)),
                    field_goals=int(game.get("FG", 0)),
                    field_goal_attempts=int(game.get("FGA", 0)),
                    field_goal_percentage=float(game.get("FG%", 0)) if game.get("FG%") else None,
                    three_pointers=int(game.get("3P", 0)),
                    three_point_attempts=int(game.get("3PA", 0)),
                    three_point_percentage=float(game.get("3P%", 0)) if game.get("3P%") else None,
                    free_throws=int(game.get("FT", 0)),
                    free_throw_attempts=int(game.get("FTA", 0)),
                    free_throw_percentage=float(game.get("FT%", 0)) if game.get("FT%") else None,
                    offensive_rebounds=int(game.get("ORB", 0)),
                    defensive_rebounds=int(game.get("DRB", 0)),
                    total_rebounds=int(game.get("TRB", 0)),
                    assists=int(game.get("AST", 0)),
                    steals=int(game.get("STL", 0)),
                    blocks=int(game.get("BLK", 0)),
                    turnovers=int(game.get("TOV", 0)),
                    personal_fouls=int(game.get("PF", 0)),
                    plus_minus=int(game.get("+/-", 0)),
                    game_score=float(game.get("GmSc", 0))
                )

                db_stats = crud.create_player_season_stats(db, stats_data, new_player.id)
                results.append(db_stats)
            except Exception as e:
                print(f"Error processing game: {e}")
                continue


@app.on_event("startup")
def initializeschedule():
    scheudler = BackgroundScheduler()
    scheudler.add_job(read_players,CronTrigger(hour=12, minute=39, second=45),timezone = "America/Virginia")
    scheudler.start()


def read_players():
    print("Cron Job Started")
    df = pd.read_csv("player.csv")
    empty_list = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
    db = next(get_db())

    try:
        last_index = 10
        for index,row in df.iterrows():
            if index ==last_index:
                time.sleep(900)
                last_index +=10
            years = []
            for i in empty_list:
                # print(row['first_name'],row['last_name'])
                stats = get_player_season_stats(row['first_name'],row['last_name'],i)
                print(stats)
                if stats:
                    print("printing to test")
                    years.append(i)
            if len(years) == 0:
                continue
            last_year = len(years)-1
            player = crud.player_record(db,row['first_name'],row['last_name'],True, years[0], years[last_year])
    except Exception as e:
        print(e)


@app.get("/players/active/{first_name}/{last_name}")
def see_active_players(first_name:str,last_name:str,db: Session = Depends(get_db)):
    player = crud.get_player(db,first_name,last_name)
    try:
        if player.is_active == 1:
            return player
        if not player:
            raise HTTPException(status_code = 404, detail = "Player not found")
    except Exception as e:
            raise HTTPException(status_code = 404, detail = f"Player not found {e}")
        

@app.get("/teams")
def teams(db: Session = Depends(get_db)):
    teams = crud.get_teams(db)
    try:
        if teams:
            return teams
        if not teams:
            raise HTTPException(status_code = 404, detail = "Teams not found")
    except Exception as e:
            raise HTTPException(status_code = 404, detail = f"Teams not found {e}")
        








@app.post("/players/{first_name}/{last_name}/{year}",response_model=List[schemas.PlayerSeasonStats])
def store_player_season_record(first_name:str, last_name:str, year:int,db:Session = Depends(get_db)):
    stats = get_player_season_stats(first_name,last_name,year)
    if not stats:
        raise HTTPException(status_code=404,detail="Player Stats not Found")
    db_player = crud.get_player(db,first_name,last_name)
    if not db_player:
        db_player = crud.create_player(db,schemas.PlayerCreate(first_name = first_name,last_name = last_name))
    results = []
    for game in stats:
        try:
            # Convert date string to date object
            game_date = datetime.strptime(game["Date"], "%Y-%m-%d").date()

            # Create stats entry
            stats_data = schemas.PlayerSeasonStatsCreate(
                date=game_date,
                team=game.get("Team", ""),
                opponent=game.get("Opp", ""),
                location=game.get("Loc", ""),
                outcome=game.get("Out", ""),
                minutes_played=game.get("MP", ""),
                points=int(game.get("PTS", 0)),
                field_goals=int(game.get("FG", 0)),
                field_goal_attempts=int(game.get("FGA", 0)),
                field_goal_percentage=float(game.get("FG%", 0)) if game.get("FG%") else None,
                three_pointers=int(game.get("3P", 0)),
                three_point_attempts=int(game.get("3PA", 0)),
                three_point_percentage=float(game.get("3P%", 0)) if game.get("3P%") else None,
                free_throws=int(game.get("FT", 0)),
                free_throw_attempts=int(game.get("FTA", 0)),
                free_throw_percentage=float(game.get("FT%", 0)) if game.get("FT%") else None,
                offensive_rebounds=int(game.get("ORB", 0)),
                defensive_rebounds=int(game.get("DRB", 0)),
                total_rebounds=int(game.get("TRB", 0)),
                assists=int(game.get("AST", 0)),
                steals=int(game.get("STL", 0)),
                blocks=int(game.get("BLK", 0)),
                turnovers=int(game.get("TOV", 0)),
                personal_fouls=int(game.get("PF", 0)),
                plus_minus=int(game.get("+/-", 0)),
                game_score=float(game.get("GmSc", 0))
            )

            db_stats = crud.create_player_season_stats(db, stats_data, db_player.id)
            results.append(db_stats)
        except Exception as e:
            print(f"Error processing game: {e}")
            continue

    return results

@app.get("/get/stats/{first_name}/{second_name}", response_model=List[schemas.PlayerSeasonStats])
def get_player_stats(first_name:str, second_name: str, skip: int = 0, limit: int = 100, db:Session = Depends(get_db)):
    player = crud.get_player(db, first_name, second_name)
    if not player:
        raise HTTPException(status_code=404,detail="Player not found")
    return crud.get_player_stats(db,player_id = player.id, skip = skip, limit = limit)


@app.post("/upload/file")
def upload(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400,detail="File not uploaded")
    
    try:
        content = file.file.read().decode("utf-8").strip()
        lines = content.split("\n")
        print(lines)
        db = next(get_db())
        for i in lines:
            full_names = i.split()
            player = crud.get_player(db, full_names[0],full_names[1])
            if player:
                player_data = get_player_season_stats(full_names[0],full_names[1],2024)
                if not player_data:
                    continue
                results = []
                for game in player_data:

                    try:
                        game_date = datetime.strptime(game["Date"], "%Y-%m-%d").date()
                        stats_data = crud.store_stats(game,game_date) 
                        db_stats = crud.create_player_season_stats(db, stats_data, player.id)
                        results.append(db_stats)
                    except Exception as e:
                        print(f"Error processing game: {e}")
                        continue
            else:
                player_data = get_player_season_stats(full_names[0],full_names[1],2024)
                if not player_data:
                    continue
                player = crud.create_player(db,schemas.PlayerCreate(first_name = full_names[0],last_name = full_names[1]))
                results = []
                for game in player_data:
                    try:
                        game_date = datetime.strptime(game["Date"], "%Y-%m-%d").date()
                        stats_data = crud.store_stats(game,game_date) 
                        db_stats = crud.create_player_season_stats(db, stats_data, player.id)
                        results.append(db_stats)
                    except Exception as e:
                        print(f"Error processing game: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"The error is {e}")
    return {"Message": "The records have been stored successfully"}
            
@app.post("/save/players")
def save_players(db:Session = Depends(get_db)):
    df = pd.read_csv("test.csv")
    empty_list = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
    try:
        for index,row in df.iterrows():
            # print(row['first_name'],row['last_name'])
            player = crud.get_player(db, row['first_name'],row['last_name'])
            player_stats = crud.get_player_from_stats(db,row['first_name'],row['last_name'])
            if player_stats:
                continue
            
            if player:
                years = []
                for i in empty_list:
                    stats = get_player_season_stats(row['first_name'],row['last_name'],i)
                    #print(stats)
                    if stats:
                        years.append(i)
                if len(years) == 0:
                    return {"Message":"Player not Found"}
                last_year = len(years)-1
                player = crud.player_record(db,row['first_name'],row['last_name'],True, years[0], years[last_year])
                return player

                
            if not player:
                crud.create_player(db,schemas.PlayerCreate(first_name = row['first_name'],last_name = row['last_name']))
                years = []
                for i in empty_list:
                    stats = get_player_season_stats(row['first_name'],row['last_name'],i)
                    #print(stats)
                    if stats:
                        years.append(i)
                if len(years) == 0:
                    return {"Message":"Player not Found"}
                last_year = len(years)-1
                player = crud.player_record(db,row['first_name'],row['last_name'],True, years[0], years[last_year])
                return player

            
    except Exception as e:
        print(f"The error is {e}")


@app.get("/see/players/stats/{first_name}/{last_name}")
def see_player_stats(first_name:str, last_name:str,db:Session = Depends(get_db)):
    try:
        player = crud.get_player_from_stats(db,first_name,last_name)
        if not player:
            return {"Message":"Player not Found"}
        return {"id":player.id,"record_found":player.record_found,"start_year":player.start_year,"end_year":player.end_year}
    except Exception as e:
        return {"Message":e}
    


@app.get("/draft-history")
def read_draft_history(db: Session = Depends(get_db)):
    stats = db.query(DraftHistory).limit(10).all()
    return stats

@app.get("/players",response_model = List[BasicPlayers])
def list_players(filters: PlayerFilter = Depends(), db: Session = Depends(get_db)):
    query = db.query(CommonPlayerInfo)
    if filters.country:
        query = query.filter(CommonPlayerInfo.country == filters.country)
    if filters.team_id:
        query = query.filter(CommonPlayerInfo.team_id == filters.team_id)
    

    result = query.limit(filters.limit).all()
    return result


@app.get("/see/players/random/info{first_name}/{last_name}")
def see_player_stats_random(first_name:str, last_name:str,db:Session = Depends(get_db)):
    player = db.query(Player).filter(Player.first_name == first_name, Player.last_name == last_name).first()
    if player:
        stat = db.query(CommonPlayerInfo).filter(CommonPlayerInfo.first_name == first_name, CommonPlayerInfo.last_name == last_name).first()
        if stat:
            draft_history = db.query(DraftHistory).filter(DraftHistory.person_id== stat.person_id).first()
            if draft_history:
                draft_combine_stats = db.query(DraftCombineStats).filter(DraftCombineStats.first_name == first_name, DraftCombineStats.last_name == last_name).first()
                if draft_combine_stats:
                     response = {"Player_name": stat.display_first_last, "Is_Active": player.is_active, "Country": stat.country, "Team_Name": stat.team_name,"Round_Number":draft_history.round_number,
                     "Round_Pick":draft_history.round_pick, "Position": draft_combine_stats.position, "Height": draft_combine_stats.height_w_shoes_ft_in, "Weight": draft_combine_stats.weight}
                     return response
                 

@app.get("/home/page/stats")
def display_home_stats(db:Session = Depends(get_db)):
    active_player = db.query(Player).filter(Player.is_active == 1).count()
    total_teams = db.query(Team).count()
    total_games = db.query(Game).count()
    return {"Active_Players": active_player, "Total_Teams": total_teams, "Total Games":total_games}


@app.get("/team/rosters")
def display_team_rosters(team_name:str, db:Session = Depends(get_db)):
    team = db.query(CommonPlayerInfo).filter(CommonPlayerInfo.team_name == team_name).all()
    empty_list = []
    for i in team:
        is_active = db.query(Player).filter(Player.full_name == i.display_first_last).first()
        if is_active.is_active == 1:
            empty_list.append(i)

    return empty_list




@app.get("/team/details")
def get_team_information(abbreviation:str, db:Session = Depends(get_db)):
    team_info = db.query(TeamDetails).filter(TeamDetails.abbreviation == abbreviation).first()
    return team_info


@app.get("/team/comparision")
def get_head_to_head_matchup(team_one: str, team_two: str, year: int, db:Session = Depends(get_db)):
    stats = db.query(Game).filter(Game.matchup_home == team_one+" "+ "vs. "+team_two).all()
    empty_list = []
    for i in stats:
        if year == i.game_date.year:
            empty_list.append(i)
        
    return empty_list
