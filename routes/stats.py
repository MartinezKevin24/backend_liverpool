from flask import Blueprint, request
from databases import db
from models.players import Stats, StatSchema

blueprint_stats = Blueprint('blueprint_stats', __name__, url_prefix='/stats')

@blueprint_stats.get('/')
def get_all_players():
  
  allStats = Stats.query.all()
  result = StatSchema().dump(allStats, many=True)
  
  return result

@blueprint_stats.post('/')
def insert_stats():
  
  #Body request parsed to JSON
  data = request.json

  #Building a Stats model with request info
  stats = Stats(
      season = data["season"],
      appearaces = data["appearaces"], 
      minutes_played = data["minutes_played"], 
      saveds = data["saveds"], 
      total_tackless = data["total_tackless"], 
      clean_sheets = data["clean_sheets"], 
      goals = data["goals"], 
      total_passes = data["total_passes"], 
      goal_assists = data["goal_assists"],
      player_id = data["player_id"]
    )
  
  #Add to database
  db.session.add(stats)
  db.session.commit()
  
  #Response to client
  return "done, stats from {} added in season {}".format(data["player_id"], data["season"])