from flask import Flask
from routes.players import blueprint_players
import sqlite3
from config import Config

db = sqlite3.connect('./databases/liverpool.db')
cursor = db.cursor()

app = Flask(__name__)
app.config.from_object(Config)

#Blueprints
app.register_blueprint(blueprint_players)

@app.route('/')
def hello():
  return "<p>Hello World<p/>"