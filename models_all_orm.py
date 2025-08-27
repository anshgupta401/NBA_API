from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Text, REAL, PrimaryKeyConstraint
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Base(DeclarativeBase):
    pass


class CommonPlayerInfo(Base):
    __tablename__ = 'common_player_info'
    person_id = Column(Text, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    display_first_last = Column(Text)
    display_last_comma_first = Column(Text)
    display_fi_last = Column(Text)
    player_slug = Column(Text)
    birthdate = Column(DateTime)
    school = Column(Text)
    country = Column(Text)
    last_affiliation = Column(Text)
    height = Column(Text)
    weight = Column(Text)
    season_exp = Column(REAL)
    jersey = Column(Text)
    position = Column(Text)
    rosterstatus = Column(Text)
    games_played_current_season_flag = Column(Text)
    team_id = Column(Integer, primary_key=True)
    team_name = Column(Text)
    team_abbreviation = Column(Text)
    team_code = Column(Text)
    team_city = Column(Text)
    playercode = Column(Text)
    from_year = Column(REAL)
    to_year = Column(REAL)
    dleague_flag = Column(Text)
    nba_flag = Column(Text)
    games_played_flag = Column(Text)
    draft_year = Column(Text)
    draft_round = Column(Text)
    draft_number = Column(Text)
    greatest_75_flag = Column(Text)



class DraftCombineStats(Base):
    __tablename__ = 'draft_combine_stats'
    season = Column(Text)
    player_id = Column(Text, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    player_name = Column(Text)
    position = Column(Text)
    height_wo_shoes = Column(REAL)
    height_wo_shoes_ft_in = Column(Text)
    height_w_shoes = Column(REAL)
    height_w_shoes_ft_in = Column(Text)
    weight = Column(Text)
    wingspan = Column(REAL)
    wingspan_ft_in = Column(Text)
    standing_reach = Column(REAL)
    standing_reach_ft_in = Column(Text)
    body_fat_pct = Column(Text)
    hand_length = Column(Text)
    hand_width = Column(Text)
    standing_vertical_leap = Column(REAL)
    max_vertical_leap = Column(REAL)
    lane_agility_time = Column(REAL)
    modified_lane_agility_time = Column(REAL)
    three_quarter_sprint = Column(REAL)
    bench_press = Column(REAL)
    spot_fifteen_corner_left = Column(Text)
    spot_fifteen_break_left = Column(Text)
    spot_fifteen_top_key = Column(Text)
    spot_fifteen_break_right = Column(Text)
    spot_fifteen_corner_right = Column(Text)
    spot_college_corner_left = Column(Text)
    spot_college_break_left = Column(Text)
    spot_college_top_key = Column(Text)
    spot_college_break_right = Column(Text)
    spot_college_corner_right = Column(Text)
    spot_nba_corner_left = Column(Text)
    spot_nba_break_left = Column(Text)
    spot_nba_top_key = Column(Text)
    spot_nba_break_right = Column(Text)
    spot_nba_corner_right = Column(Text)
    off_drib_fifteen_break_left = Column(Text)
    off_drib_fifteen_top_key = Column(Text)
    off_drib_fifteen_break_right = Column(Text)
    off_drib_college_break_left = Column(Text)
    off_drib_college_top_key = Column(Text)
    off_drib_college_break_right = Column(Text)
    on_move_fifteen = Column(Text)
    on_move_college = Column(Text)



class DraftHistory(Base):
    __tablename__ = 'draft_history'
    person_id = Column(Text, primary_key=True)
    player_name = Column(Text)
    season = Column(Text)
    round_number = Column(Integer)
    round_pick = Column(Integer)
    overall_pick = Column(Integer)
    draft_type = Column(Text)
    team_id = Column(Text, primary_key=True)
    team_city = Column(Text)
    team_name = Column(Text)
    team_abbreviation = Column(Text)
    organization = Column(Text)
    organization_type = Column(Text)
    player_profile_flag = Column(Text)



class Game(Base):
    __tablename__ = 'game'
    season_id = Column(Text, primary_key=True)
    team_id_home = Column(Text)
    team_abbreviation_home = Column(Text)
    team_name_home = Column(Text)
    game_id = Column(Text, primary_key=True)
    game_date = Column(DateTime)
    matchup_home = Column(Text)
    wl_home = Column(Text)
    min = Column(Integer)
    fgm_home = Column(REAL)
    fga_home = Column(REAL)
    fg_pct_home = Column(REAL)
    fg3m_home = Column(REAL)
    fg3a_home = Column(REAL)
    fg3_pct_home = Column(REAL)
    ftm_home = Column(REAL)
    fta_home = Column(REAL)
    ft_pct_home = Column(REAL)
    oreb_home = Column(REAL)
    dreb_home = Column(REAL)
    reb_home = Column(REAL)
    ast_home = Column(REAL)
    stl_home = Column(REAL)
    blk_home = Column(REAL)
    tov_home = Column(REAL)
    pf_home = Column(REAL)
    pts_home = Column(REAL)
    plus_minus_home = Column(Integer)
    video_available_home = Column(Integer)
    team_id_away = Column(Text)
    team_abbreviation_away = Column(Text)
    team_name_away = Column(Text)
    matchup_away = Column(Text)
    wl_away = Column(Text)
    fgm_away = Column(REAL)
    fga_away = Column(REAL)
    fg_pct_away = Column(REAL)
    fg3m_away = Column(REAL)
    fg3a_away = Column(REAL)
    fg3_pct_away = Column(REAL)
    ftm_away = Column(REAL)
    fta_away = Column(REAL)
    ft_pct_away = Column(REAL)
    oreb_away = Column(REAL)
    dreb_away = Column(REAL)
    reb_away = Column(REAL)
    ast_away = Column(REAL)
    stl_away = Column(REAL)
    blk_away = Column(REAL)
    tov_away = Column(REAL)
    pf_away = Column(REAL)
    pts_away = Column(REAL)
    plus_minus_away = Column(Integer)
    video_available_away = Column(Integer)
    season_type = Column(Text)



class GameInfo(Base):
    __tablename__ = 'game_info'
    game_id = Column(Text, primary_key=True)
    game_date = Column(DateTime)
    attendance = Column(Integer)
    game_time = Column(Text)



class GameSummary(Base):
    __tablename__ = 'game_summary'
    game_date_est = Column(DateTime)
    game_sequence = Column(Integer)
    game_id = Column(Text, primary_key=True)
    game_status_id = Column(Integer, primary_key=True)
    game_status_text = Column(Text)
    gamecode = Column(Text)
    home_team_id = Column(Text, primary_key=True)
    visitor_team_id = Column(Text, primary_key=True)
    season= Column(Text)
    live_period = Column(Integer)
    live_pc_time = Column(Text)
    natl_tv_broadcaster_abbreviation = Column(Text)
    live_period_time_bcast = Column(Text)
    wh_status = Column(Integer)



class InactivePlayers(Base):
    __tablename__ = 'inactive_players'
    game_id = Column(Text, primary_key=True)
    player_id = Column(Text, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    jersey_num = Column(Text)
    team_id = Column(Text, primary_key=True)
    team_city = Column(Text)
    team_name = Column(Text)
    team_abbreviation = Column(Text)



class LineScore(Base):
    __tablename__ = 'line_score'
    game_date_est = Column(DateTime)
    game_sequence = Column(Integer)
    game_id = Column(Text, primary_key=True)
    team_id_home = Column(Text)
    team_abbreviation_home = Column(Text)
    team_city_name_home = Column(Text)
    team_nickname_home = Column(Text)
    team_wins_losses_home = Column(Text)
    pts_qtr1_home = Column(Text)
    pts_qtr2_home = Column(Text)
    pts_qtr3_home = Column(Text)
    pts_qtr4_home = Column(Text)
    pts_ot1_home = Column(Integer)
    pts_ot2_home = Column(Integer)
    pts_ot3_home = Column(Integer)
    pts_ot4_home = Column(Integer)
    pts_ot5_home = Column(Integer)
    pts_ot6_home = Column(Integer)
    pts_ot7_home = Column(Integer)
    pts_ot8_home = Column(Integer)
    pts_ot9_home = Column(Integer)
    pts_ot10_home = Column(Integer)
    pts_home = Column(REAL)
    team_id_away = Column(Text)
    team_abbreviation_away = Column(Text)
    team_city_name_away = Column(Text)
    team_nickname_away = Column(Text)
    team_wins_losses_away = Column(Text)
    pts_qtr1_away = Column(Integer)
    pts_qtr2_away = Column(Text)
    pts_qtr3_away = Column(Text)
    pts_qtr4_away = Column(Integer)
    pts_ot1_away = Column(Integer)
    pts_ot2_away = Column(Integer)
    pts_ot3_away = Column(Integer)
    pts_ot4_away = Column(Integer)
    pts_ot5_away = Column(Integer)
    pts_ot6_away = Column(Integer)
    pts_ot7_away = Column(Integer)
    pts_ot8_away = Column(Integer)
    pts_ot9_away = Column(Integer)
    pts_ot10_away = Column(Integer)
    pts_away = Column(REAL)



class Officials(Base):
    __tablename__ = 'officials'
    game_id = Column(Text, primary_key=True)
    official_id = Column(Text, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    jersey_num = Column(Text)



class OtherStats(Base):
    __tablename__ = 'other_stats'
    game_id = Column(Text, primary_key=True)
    league_id = Column(Text, primary_key=True)
    team_id_home = Column(Text)
    team_abbreviation_home = Column(Text)
    team_city_home = Column(Text)
    pts_paint_home = Column(Integer)
    pts_2nd_chance_home = Column(Integer)
    pts_fb_home = Column(Integer)
    largest_lead_home = Column(Integer)
    lead_changes = Column(Integer)
    times_tied = Column(Integer)
    team_turnovers_home = Column(Integer)
    total_turnovers_home = Column(Integer)
    team_rebounds_home = Column(Integer)
    pts_off_to_home = Column(Integer)
    team_id_away = Column(Text)
    team_abbreviation_away = Column(Text)
    team_city_away = Column(Text)
    pts_paint_away = Column(Integer)
    pts_2nd_chance_away = Column(Integer)
    pts_fb_away = Column(Integer)
    largest_lead_away = Column(Integer)
    team_turnovers_away = Column(Integer)
    total_turnovers_away = Column(Integer)
    team_rebounds_away = Column(Integer)
    pts_off_to_away = Column(Integer)



class PlayByPlay(Base):
    __tablename__ = 'play_by_play'
    game_id = Column(Text, primary_key=True)
    eventnum = Column(Integer)
    eventmsgtype = Column(Integer)
    eventmsgactiontype = Column(Integer)
    period = Column(Integer)
    wctimestring = Column(Text)
    pctimestring = Column(Text)
    homedescription = Column(Text)
    neutraldescription = Column(Text)
    visitordescription = Column(Text)
    score = Column(Text)
    scoremargin = Column(Text)
    person1type = Column(REAL)
    player1_id = Column(Text, primary_key=True)
    player1_name = Column(Text)
    player1_team_id = Column(Text, primary_key=True)
    player1_team_city = Column(Text)
    player1_team_nickname = Column(Text)
    player1_team_abbreviation = Column(Text)
    person2type = Column(REAL)
    player2_id = Column(Text, primary_key=True)
    player2_name = Column(Text)
    player2_team_id = Column(Text, primary_key=True)
    player2_team_city = Column(Text)
    player2_team_nickname = Column(Text)
    player2_team_abbreviation = Column(Text)
    person3type = Column(REAL)
    player3_id = Column(Text, primary_key=True)
    player3_name = Column(Text)
    player3_team_id = Column(Text, primary_key=True)
    player3_team_city = Column(Text)
    player3_team_nickname = Column(Text)
    player3_team_abbreviation = Column(Text)
    video_available_flag = Column(Text)



class Player(Base):
    __tablename__ = 'player'
    id = Column(Text, primary_key=True)
    full_name = Column(Text)
    first_name = Column(Text)
    last_name = Column(Text)
    is_active = Column(Integer)



class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    full_name = Column(Text)
    abbreviation = Column(Text)
    nickname = Column(Text)
    city = Column(Text)
    state = Column(Text)
    year_founded = Column(REAL)



class TeamDetails(Base):
    __tablename__ = 'team_details'
    team_id = Column(Text, primary_key=True)
    abbreviation = Column(Text)
    nickname = Column(Text)
    yearfounded = Column(REAL)
    city = Column(Text)
    arena = Column(Text)
    arenacapacity = Column(REAL)
    owner = Column(Text)
    generalmanager = Column(Text)
    headcoach = Column(Text)
    dleagueaffiliation = Column(Text)
    facebook = Column(Text)
    instagram = Column(Text)
    twitter = Column(Text)



class TeamHistory(Base):
    __tablename__ = 'team_history'
    team_id = Column(Text, primary_key=True)
    city = Column(Text)
    nickname = Column(Text)
    year_founded = Column(Integer)
    year_active_till = Column(Integer)



class TeamInfoCommon(Base):
    __tablename__ = 'team_info_common'
    team_id = Column(Text, primary_key=True)
    season_year = Column(Text)
    team_city = Column(Text)
    team_name = Column(Text)
    team_abbreviation = Column(Text)
    team_conference = Column(Text)
    team_division = Column(Text)
    team_code = Column(Text)
    team_slug = Column(Text)
    w = Column(Integer)
    l = Column(Integer)
    pct = Column(REAL)
    conf_rank = Column(Integer)
    div_rank = Column(Integer)
    min_year = Column(Integer)
    max_year = Column(Integer)
    league_id = Column(Text, primary_key=True)
    season_id = Column(Text, primary_key=True)
    pts_rank = Column(Integer)
    pts_pg = Column(REAL)
    reb_rank = Column(Integer)
    reb_pg = Column(REAL)
    ast_rank = Column(Integer)
    ast_pg = Column(REAL)
    opp_pts_rank = Column(Integer)
    opp_pts_pg = Column(REAL)

