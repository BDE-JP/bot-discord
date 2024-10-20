
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

ALTER TABLE users ADD COLUMN first_name TEXT;
ALTER TABLE users ADD COLUMN last_name TEXT;
ALTER TABLE users ADD COLUMN identifier TEXT;
ALTER TABLE users ADD COLUMN email TEXT;

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