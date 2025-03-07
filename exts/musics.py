# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import requests
import lichess.api

from ..__base__ import library_sn; discord = library_sn.discord
from .. import database


def add_music(user, activity):

    if activity.duration < datetime.timedelta(minutes=1):
        return

    print(
        user.id,
        user.name,
        activity.title,
        activity.artists,
        activity.album,
        activity.album_cover_url,
        activity.track_url
    )

    database.musics.add_music((
        user.id,
        user.name,
        activity.title,
        activity.artists,
        activity.album,
        activity.album_cover_url,
        activity.track_url
    ))


def today():

    music = random.choice(list(database.musics.get_all().fetchall()))

    (
        user_id,
        user_name,
        title,
        artists,
        album,
        album_cover_url,
        track_url
    ) = music

    embed = discord.Embed(
        title = "Musique du jour :",
        description = f"[**{title}**]({track_url})\n{artists}\n_{album}_"
    )
    embed.set_thumbnail(album_cover_url)

    database.musics.delete_all()

    return embed