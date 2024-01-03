DROP TABLE IF EXISTS stats;

CREATE TABLE stats (
    stats_id INTEGER PRIMARY KEY AUTOINCREMENT,
    appearaces INTEGER NOT NULL,
    minutes_played INTEGER NOT NULL,
    saveds INTEGER NOT NULL,
    total_tackless INTEGER NOT NULL,
    clean_sheets INTEGER NOT NULL,
    goals INTEGER NOT NULL,
    total_passes INTEGER NOT NULL,
    goal_assists INTEGER NOT NULL
);

DROP TABLE IF EXISTS seasons;

CREATE TABLE seasons (
    season_id INTEGER PRIMARY KEY AUTOINCREMENT,
    season TEXT NOT NULL,
    stats_id INTEGER,
    FOREIGN KEY(stats_id) REFERENCES stats(stats_id)
);

DROP TABLE IF EXISTS players;

CREATE TABLE players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT NOT NULL,
    player_last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    dorsal INTEGER NOT NULL,
    lastest_team TEXT NOT NULL,
    photo_shield_lastest_team TEXT,
    photo TEXT NOT NULL,
    incorporation_date TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    nationality TEXT NOT NULL,
    season_id INTEGER,
    FOREIGN KEY(season_id) REFERENCES seasons(season_id)
);