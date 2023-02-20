from models.map.Map import Map
from models.user.User import User
from models.match.Match import Match
from models.match.MatchUser import MatchUser
from models.match.MatchRound import MatchRound
from datetime import datetime
from typing import List

def add_match_to_db(created_by_user:User,
              ranked_flag:bool, 
              map_played:Map,
              date_match_played:datetime,
              match_users:List[MatchUser],
              match_rounds:List[MatchRound],
              db):

    match = Match(created_by_user_id=created_by_user.id, 
                          ranked_flag=ranked_flag, 
                          map_played=map_played, 
                          date_match_played=date_match_played)

    db.session.add(match)
    db.session.commit()