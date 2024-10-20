SELECT
	id,
	channel_id,
	message_id,
	user_id,
	first_name,
	last_name,
	identifier
FROM verifications
WHEN message_id = ?