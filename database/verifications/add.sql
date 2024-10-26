
INSERT OR IGNORE INTO verifications (
	channel_id,
	message_id, 
	user_id,
	last_name,
	first_name, 
	identifier
)
VALUES (
    ?,
    ?,
    ?,
    ?,
    ?,
    ?
)
