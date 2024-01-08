from flask import Blueprint, request
from databases import db
from models.players import Stats, StatSchema
from markupsafe import escape
import collections.abc

blueprint_stats = Blueprint('blueprint_stats', __name__, url_prefix='/stats')

@blueprint_stats.get('/')
def get_all_stats():
  
  #Get all stats from database
  allStats = Stats.query.all()
  #Serialize array with all stats
  result = StatSchema().dump(allStats, many=True)
  #Return all stats in JSON format
  return result

@blueprint_stats.post('/')
def insert_stats():
  
  #Body request parsed to JSON
  body = request.json
  
  if not isinstance(body, collections.abc.Sequence):
    return "Data format is not valid"
  
  for data in body:
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
        player_id = data["player_id"],
        season_number = data["season_number"],
        successful_dribbles = data["successful_dribbles"],
        tackles_won = data["tackles_won"],
        total_shots = data["total_shots"],
        interceptions = data["interceptions"],
        yellow_cards = data["yellow_cards"],
        red_cards = data["red_cards"],
        foul_conceded = data["foul_conceded"],
        starts = data["starts"],
        substituted_on = data["substituted_on"]
      )
    
    print(data)
    #Add to database
    db.session.add(stats)
    db.session.commit()

  #Response to client
  return "done, stats from {} added".format(data["player_id"])

@blueprint_stats.put('/<id>')
def update_stat(id):
  
  print(id)
  
  #Find Stat in database with id
  stat = Stats.query.filter_by(stat_id = escape(id)).first()
  
  #Valdiate if player exist
  if stat:
    #Iterate through all items in the request body.
    for key, value in request.json.items():
      #Validate if player has this attribute
      if hasattr(stat, key):
        #Change that attribute
        setattr(stat, key, value)

    #Add updated player to database
    db.session.commit()
    
    #Return success message
    return "done, data from stat id {} season {} updated".format(stat.stat_id, stat.season)
  
  else:
    #Return failure message
    return "Stat doesn't exist yet."