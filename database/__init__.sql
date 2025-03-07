
CREATE TABLE IF NOT EXISTS users 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_id INTEGER UNIQUE,
    lichess_pseudo TEXT,
    minecraft_pseudo TEXT,
    first_name TEXT,
    last_name TEXT,
    identifier TEXT UNIQUE,
    email TEXT,
    created_at DATE
);

CREATE TABLE IF NOT EXISTS verifications 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    channel_id INTEGER,
    message_id INTEGER,
    user_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    identifier TEXT
);


CREATE TABLE IF NOT EXISTS musics 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    user_name TEXT,
    title TEXT,
    artists TEXT,
    album TEXT,
    album_cover_url TEXT,
    track_url TEXT
);
