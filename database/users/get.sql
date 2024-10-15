
SELECT
  id,
  discord_id,
  lichess_pseudo,
  minecraft_pseudo
FROM users
WHERE discord_id = ?
