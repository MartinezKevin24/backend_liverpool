from flask import Blueprint, request
from databases import db
from models.players import Stats, Players

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

@blueprint_players.get('/')
def get_all_players():
  # player_stats = player_stats(request.json["stats"])
  # return db.session.add([player_info, player_stats])
  return 'Get all players'
  
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