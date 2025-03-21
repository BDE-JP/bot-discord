# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import random
import requests
import datetime
import lichess.api

from ..__base__ import library_sn; discord = library_sn.discord
from .. import database


def add_music(user, activity):

    if (
        (activity.start.replace(tzinfo=None) + datetime.timedelta(minutes=1))
        > datetime.datetime.utcnow().replace(tzinfo=None)
    ):
        return

    database.musics.add_music((
        user.id,
        user.name,
        activity.title,
        ', '.join(activity.artists),
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
        description = f"[**{title}**]({track_url})\n{artists}\n_{album}_\n\nÉcoutée par : <@{user_id}>"
    )
    embed.set_thumbnail(url=album_cover_url)

    database.musics.delete_all()

    return embed
