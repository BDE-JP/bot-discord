
UPDATE users
SET last_name = ?,
    first_name = ?,
    identifier = ?
WHERE users.discord_id = ?
