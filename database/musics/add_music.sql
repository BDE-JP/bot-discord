INSERT OR IGNORE TO musics (
    user_id,
    user_name,
    title,
    artists,
    album,
    album_cover_url,
    track_url
) VALUES (
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?
)