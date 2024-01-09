from flask import Blueprint, request
from databases import db
from models.players import Stats, StatSchema
from markupsafe import escape
import collections.abc
from sqlalchemy import delete

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
  
  #Find Stat in database with id
  stat = db.get_or_404(Stats, id)

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
  
@blueprint_stats.delete('/<id>/delete')
def delete_stat(id):
  
  #Find Stat in database with id
  stat = db.get_or_404(Stats, escape(id))
  
  #Delete from database
  db.session.delete(stat)
  db.session.commit()
  
  #Return success message
  return "success, stat deleted"

@blueprint_stats.post('/delete/')
def delete_stats():
  
  #Body request parsed to JSON
  body = request.json
  
  if not isinstance(body, collections.abc.Sequence):
    return "Data format is not valid"
  
  #Iterate body request
  for stat in body:
    
    #Search stat with id column
    stat = db.get_or_404(Stats, stat)
    
    #Delete from database one by one
    db.session.delete(stat)
    db.session.commit()
  
  #Return success message
  return"Success"

@blueprint_stats.delete('/<player_id>/alldelete/')
def delete_all_stats(player_id):
  
  #Search for a row with row with the value of the entered player_id parameter
  result = db.session.query(Stats).filter(Stats.player_id == escape(player_id)).first()
  
  #Validate if at least one row exist
  if result != None:
    #Delete all rows with that player_id parameter
    db.session.execute(delete(Stats).where(Stats.player_id == escape(player_id)))
    db.session.commit()
    #Return success message
    return "All Stats deleted from {}".format(escape(player_id))
  
  #Return failure message
  else:
    return "Stats for {} not exist".format(escape(player_id)) 
