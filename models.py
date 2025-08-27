from sqlalchemy import Column,Integer,String,Float,Date,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from database import Base

class Player(Base):
    __tablename__ = "Players"
    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String,index=True)
    last_name = Column(String,index=True)
    stats = relationship("PlayerSeasonStats", back_populates="player")  

class PlayerSeasonStats(Base):
    __tablename__ = "player_season_stats"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("Players.id"))
    date = Column(Date)
    team = Column(String)
    opponent = Column(String)
    location = Column(String)
    outcome = Column(String)
    minutes_played = Column(String)
    points = Column(Integer)
    field_goals = Column(Integer)
    field_goal_attempts = Column(Integer)
    field_goal_percentage = Column(Float)
    three_pointers = Column(Integer)
    three_point_attempts = Column(Integer)
    three_point_percentage = Column(Float)
    free_throws = Column(Integer)
    free_throw_attempts = Column(Integer)
    free_throw_percentage = Column(Float)
    offensive_rebounds = Column(Integer)
    defensive_rebounds = Column(Integer)
    total_rebounds = Column(Integer)
    assists = Column(Integer)
    steals = Column(Integer)
    blocks = Column(Integer)
    turnovers = Column(Integer)
    personal_fouls = Column(Integer)
    plus_minus = Column(Integer)
    game_score = Column(Float)

    player = relationship("Player", back_populates="stats")


class PlayerStats(Base):
    __tablename__ = "players_record"
    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String,index=True)
    last_name = Column(String,index=True)
    record_found = Column(Boolean)
    start_year = Column(Integer)
    end_year = Column(Integer)
