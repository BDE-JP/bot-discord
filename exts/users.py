# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import requests
import lichess.api

from .. import database


CACHE_ELO = {}
CACHE_ONLINE_MINECRAFT = []


class User:

    def __init__(self, data):

        (
            self.id,
            self.discord_id,
            self.lichess_pseudo,
            self.minecraft_pseudo
        ) = data

    def set_pseudo_lichess(self, pseudo:str):
        database.users.set_pseudo_lichess((pseudo, self.id))

    def set_pseudo_minecraft(self, pseudo:str):
        database.users.set_pseudo_minecraft((pseudo, self.id))


def get(discord_id:int, *, refresh=False):

    data = database.users.get(discord_id).fetchone()

    if data:
        return User(data)
    elif not refresh:
        database.users.create(discord_id)
        return get(discord_id, refresh=True)


def get_data_server_minecraft() -> dict:

    response = requests.get(
        "https://api.mcstatus.io/v2/status/java/5.196.4.146"
    )

    if response.status_code != 200:
        return {}

    return response.json()


def online_minecraft() -> list:

    online = []

    users = [get(uid) for (uid,) in database.users.all().fetchall()]

    data = get_data_server_minecraft()

    pseudos = [
        v["name_clean"]
        for v in data.get("players", {}).get("list", [])
    ]

    for user in users:

        if not user.minecraft_pseudo:
            continue

        if (
            user.minecraft_pseudo in pseudos 
            and user.minecraft_pseudo not in CACHE_ONLINE_MINECRAFT
        ):
            CACHE_ONLINE_MINECRAFT.append(user.minecraft_pseudo)
            online.append((user, True))

        if (
            user.minecraft_pseudo not in pseudos 
            and user.minecraft_pseudo in CACHE_ONLINE_MINECRAFT
        ):
            CACHE_ONLINE_MINECRAFT.remove(user.minecraft_pseudo)
            online.append((user, False))

    return online


def get_new_elo() -> list:

    elo = []

    data = [get(uid) for (uid,) in database.users.all().fetchall()]

    for user in data:

        if not user.lichess_pseudo:
            continue

        perfs = lichess.api.user(user.lichess_pseudo).get("perfs")

        for name in ["blitz", "bullet", "rapid", "classical"]:
            if user.id not in CACHE_ELO:
                continue

            old = CACHE_ELO[user.id][name]["rating"]
            new = perfs[name]["rating"]

            if new != old:
                elo.append((user.discord_id, name, old, new))

        CACHE_ELO[user.id] = perfs

    return elo
