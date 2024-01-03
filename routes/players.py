from flask import Blueprint, current_app, request
import sqlite3 as sql

blueprint_players = Blueprint('blueprint_players', __name__, url_prefix='/players')

@blueprint_players.route('/', methods=['GET', 'POST'])
def get_all_players():
  db = sql.connect(current_app.config['DB_PATH'])
  if request.method == "POST":
    appearaces = request.json['appearaces']
    minutes_played = request.json['minutes_played']
    saveds = request.json['saveds']
    total_tackless = request.json['total_tackless']
    clean_sheets = request.json['clean_sheets']
    goals = request.json['goals']
    total_passes = request.json['total_passes']
    goal_assists = request.json['goal_assists']
    data = request.json
    db.execute('INSERT INTO stats (appearaces, minutes_played, saveds, total_tackless, clean_sheets, goals, total_passes, goal_assists) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (appearaces, minutes_played, saveds, total_tackless, clean_sheets, goals, total_passes, goal_assists))
    db.commit()
    db.close()
    return data
  else:
    return "get"