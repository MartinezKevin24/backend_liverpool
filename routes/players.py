from flask import Blueprint, request, jsonify
from databases import db
from models.players import Stats, Players, PlayerSchema, StatSchema
from markupsafe import escape

blueprint_players = Blueprint('blueprint_players', __name__, url_prefix='/players')

def player(data):
  return  

# def player_stats(data):
#   return Stats(
#       season = data['season'],
#       appearaces = data['appearaces'],
#       minutes_played = data['minutes_played'],
#       saveds = data['saveds'],
#       dorsal = data['dorsal'],
#       total_tackless = data['total_tackless'],
#       clean_sheets = data['clean_sheets'],
#       goals = data['goals'],
#       total_passes = data['total_passes'],
#       goal_assists = data['goal_assists'],
#       player_id = data['player_id'],
#     )

@blueprint_players.get('/<id>')
def get_player_detail(id):
  
  data = db.session.query(Players).filter(Players.player_id == escape(id)).first()
  stats = db.session.query(Stats).filter(Stats.player_id == escape(id)).all()
  print(data, stats)  
  return {
    "player": PlayerSchema().dump(data),
    "stats": StatSchema().dump(stats, many=True)
  }

@blueprint_players.get('/')
def get_all_players():
  
  #Get all players from database
  allPlayers = Players.query.all()
  #Serialize array with all players
  result = PlayerSchema().dump(allPlayers, many=True)
  #Return all players in JSON format
  return result
  
@blueprint_players.post('/')
def insert_player():
  
  #Body request parsed to JSON
  data = request.json

  #Building a Player model with request info
  player_info = Players(
      player_id = data['player_id'],
      player_name = data['player_name'],
      player_last_name = data['player_last_name'],
      age = data['age'],
      dorsal = data['dorsal'],
      lastest_team = data['lastest_team'],
      photo_shield_lastest_team = data.get('photo_shield_lastest_team', None),
      photo = data['photo'],
      incorporation_date = data['incorporation_date'],
      birth_date = data['birth_date'],
      nationality = data['nationality'],
      position = data["position"]
    )
  
  #Add to database
  db.session.add(player_info)
  db.session.commit()
  
  #Response to client
  return "done, data from player {} {} added".format(data['player_name'], data['player_last_name'])

@blueprint_players.put('/<id>')
def update_player(id):
  
  #Find player in database with id
  player = Players.query.filter_by(player_id = escape(id)).first()
  
  #Valdiate if player exist
  if player:
    #Iterate through all items in the request body.
    for key, value in request.json.items():
      #Validate if player has this attribute
      if hasattr(player, key):
        #Change that attribute
        setattr(player, key, value)

    #Add updated player to database
    db.session.commit()
    
    #Return success message
    return "done, data from player {} {} updated".format(player.player_name, player.player_last_name)
  
  else:
    #Return failure message
    return "player doesn't exist yet."