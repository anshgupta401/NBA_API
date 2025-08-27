from pydantic import BaseModel
from datetime import date
from typing import Optional

class PlayerCreate(BaseModel):
    first_name: str
    last_name: str

class PlayerSeasonStatsCreate(BaseModel):
    date: date
    team: str
    opponent: str
    location: str
    outcome: str
    minutes_played: str
    points: int
    field_goals: int
    field_goal_attempts: int
    field_goal_percentage: Optional[float] = None
    three_pointers: int
    three_point_attempts: int
    three_point_percentage: Optional[float] = None
    free_throws: int
    free_throw_attempts: int
    free_throw_percentage: Optional[float] = None
    offensive_rebounds: int
    defensive_rebounds: int
    total_rebounds: int
    assists: int
    steals: int
    blocks: int
    turnovers: int
    personal_fouls: int
    plus_minus: int
    game_score: float


class PlayerSeasonStats(PlayerSeasonStatsCreate):
    id: int
    player_id: int
    class Config:
        orm_mode = True


class PlayerFilter(BaseModel):
    country: Optional[str] = None
    team_id: Optional[str] = None
    limit: int = 20


class BasicPlayers(BaseModel):
    person_id: str
    display_first_last: Optional[str] = None
    country: Optional[str] = None
    team_id: Optional[int] = None
    class Config:
        from_attributes = True
