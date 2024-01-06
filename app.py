from flask import Flask
from routes.players import blueprint_players
from routes.stats import blueprint_stats
from config import Config
from databases import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from models import players

with app.app_context():
    db.create_all()

#Blueprints
app.register_blueprint(blueprint_players)
app.register_blueprint(blueprint_stats)

@app.route('/')
def hello():
  return "<p>Hello World<p/>"