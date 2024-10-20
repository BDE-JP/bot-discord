
INSERT OR IGNORE INTO verifications (
	channel_id,
	message_id, 
	user_id,
	first_name, 
	last_name, 
	identifier
)
VALUES (
    ?,
    ?,
    ?,
    ?,
    ?
)
