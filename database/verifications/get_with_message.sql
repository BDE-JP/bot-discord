SELECT
	id,
	channel_id,
	message_id,
	user_id,
	last_name,
	first_name,
	identifier
FROM verifications
WHERE message_id = ?
