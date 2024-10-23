
UPDATE users
SET first_name = ?,
	last_name = ?,
	identifier = ?
WHERE users.discord_id = ?
