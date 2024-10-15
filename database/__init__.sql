
CREATE TABLE IF NOT EXISTS users 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_id INTEGER UNIQUE,
    lichess_pseudo TEXT,
    minecraft_pseudo TEXT,
    created_at DATE
);


CREATE TABLE IF NOT EXISTS identities 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_id INTEGER UNIQUE,
    first_name TEXT,
    last_name TEXT,
    identifier INTEGER UNIQUE,
    email TEXT,
    created_at DATE
);

