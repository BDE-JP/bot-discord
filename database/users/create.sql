
INSERT OR IGNORE INTO users (
    discord_id,
    created_at
)
VALUES (
    ?,
    strftime('%Y-%m-%d %H:%M:%S', 'now')
)
