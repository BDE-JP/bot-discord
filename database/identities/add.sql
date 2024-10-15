
INSERT OR IGNORE INTO identities (
    discord_id,
    first_name,
    last_name,
    identifier,
    created_at
)
VALUES (
    ?,
    ?,
    ?,
    ?,
    strftime('%Y-%m-%d %H:%M:%S', 'now')
)
