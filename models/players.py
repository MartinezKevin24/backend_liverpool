from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from databases import db

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