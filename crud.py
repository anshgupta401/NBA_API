from sqlalchemy.orm import Session
import models,schemas
from models_all_orm import *

def get_player(db:Session, first_name: str, last_name: str):
    return db.query(Player).filter(Player.first_name == first_name, Player.last_name == last_name).first()

def get_teams(db:Session):
    return db.query(Team).all()


def create_player(db:Session, player:schemas.PlayerCreate):
    db_player = models.Player(first_name = player.first_name, last_name = player.last_name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def create_player_season_stats(db:Session,stats:schemas.PlayerSeasonStatsCreate,player_id:int):
    stats = models.PlayerSeasonStats(player_id = player_id, **stats.dict())
    db.add(stats)
    db.commit()
    db.refresh(stats)
    return stats

def get_player_stats(db:Session, player_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.PlayerSeasonStats).filter(models.PlayerSeasonStats.player_id == player_id).offset(skip).limit(limit).all()

def store_stats(game,game_date):
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
    return stats_data

def player_record(db:Session, first_name: str, last_name: str, record_found: bool, start_year: int, end_year: int):
    player = models.PlayerStats(first_name = first_name, last_name = last_name, record_found = record_found, start_year = start_year, end_year = end_year)
    db.add(player)
    db.commit()
    db.refresh(player)
    return player


def get_player_from_stats(db:Session, first_name: str, last_name: str):
    return db.query(models.PlayerStats).filter(models.PlayerStats.first_name == first_name, models.PlayerStats.last_name == last_name).first()
