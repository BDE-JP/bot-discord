SELECT
	id,
	channel_id,
	message_id,
	user_id,
	first_name,
	last_name,
	identifier
FROM verifications
WHERE message_id = ?
