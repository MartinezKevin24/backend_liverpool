from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from databases import db
from marshmallow import Schema, fields

class Stats(db.Model):
  __tablename__: "stats"
  stat_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
  season: Mapped[str] = mapped_column(String, nullable=False)
  appearaces: Mapped[int] = mapped_column(Integer, nullable=False)
  minutes_played: Mapped[int] = mapped_column(Integer, nullable=False)
  saveds: Mapped[int] = mapped_column(Integer, nullable=True)
  total_tackless: Mapped[int] = mapped_column(Integer, nullable=True)
  clean_sheets: Mapped[int] = mapped_column(Integer, nullable=True)
  goals: Mapped[int] = mapped_column(Integer, nullable=True)
  total_passes: Mapped[int] = mapped_column(Integer, nullable=True)
  goal_assists: Mapped[int] = mapped_column(Integer, nullable=True)
  player_id: Mapped[int] = mapped_column(ForeignKey("players.player_id"), nullable=False)
  
  def __str__(self):
    info = "Temporada: {}, apariciones: {}, minutos jugados: {}, salvadas: {}, barridas totales: {}, porterias imbatidas: {}, goles: {}, pases totales: {}, goles totales: {}, jugador: {}".format(self.season, self.appearaces, self.minutes_played, self.saveds, self.total_tackless, self.clean_sheets, self.goals, self.total_passes, self.goal_assists, self.player_id)
    return info
  
class Players(db.Model):
  __tablename__: "players"
  player_id: Mapped[str] = mapped_column(String, primary_key=True, nullable=False)
  player_name: Mapped[str] = mapped_column(String, nullable=False)
  player_last_name: Mapped[str] = mapped_column(String, nullable=False)
  age: Mapped[int] = mapped_column(Integer, nullable=False)
  dorsal: Mapped[int] = mapped_column(Integer, nullable=False)
  lastest_team: Mapped[str] = mapped_column(String, nullable=False)
  photo_shield_lastest_team: Mapped[str] = mapped_column(String, nullable=True)
  photo: Mapped[str] = mapped_column(String, nullable=False)
  incorporation_date: Mapped[str] = mapped_column(String, nullable=False)
  birth_date: Mapped[str] = mapped_column(String, nullable=False)
  nationality: Mapped[str] = mapped_column(String, nullable=False)
  position: Mapped[str] = mapped_column(String, nullable=False)
  
  def __str__(self):
    info = "Jugador: {} {}, edad: {}, feha nacimiento: {}, foto: {}, dorsal: {}, ultimo equipo: {}, foto escudo ultimo equipo: {}, fehca de incorporacion: {}, nacionalidad: {}, posición: {}".format(self.player_name, self.player_last_name, self.age, self.birth_date, self.photo, self.dorsal, self.lastest_team, self.photo_shield_lastest_team, self.incorporation_date, self.nationality, self.position)
    return info
  
class PlayerSchema(Schema):
  player_id = fields.Str()
  player_name = fields.Str()
  player_last_name = fields.Str()
  age = fields.Int()
  dorsal = fields.Int()
  lastest_team = fields.Str()
  photo_shield_lastest_team = fields.Str()
  photo = fields.Str()
  incorporation_date = fields.Str()
  birth_date = fields.Str()
  nationality = fields.Str()
  position = fields.Str()

class StatSchema(Schema):
  season = fields.Str()
  appearaces = fields.Int() 
  minutes_played = fields.Int() 
  saveds = fields.Int() 
  total_tackless = fields.Int() 
  clean_sheets = fields.Int()  
  goals = fields.Int() 
  total_passes = fields.Int()  
  goal_assists = fields.Int() 
  player_id = fields.Str()