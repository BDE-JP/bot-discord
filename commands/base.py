# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import requests
import lichess.api

from ..__base__ import manage
from ..exts import users


Command = manage.commands.Command
commands = manage.commands.Commands()


@commands.add
def ping(ctx):
    ctx.response(description="pong")


@commands.add
def pseudo(ctx, domain:str, name:str):
    user = users.get(ctx.author.id)

    if domain == "lichess" and user and lichess.api.user(name):
        user.set_pseudo_lichess(name)
        ctx.response(description="Pseudo mis à jour !")

    elif domain == "minecraft" and user:
        user.set_pseudo_minecraft(name)
        ctx.response(description="Pseudo mis à jour !")

    else:
        ctx.response(
            description= \
                "Merci de mettre un pseudo minecraft ou lichess valide !"
        )


@commands.add
def minecraft(ctx):

    response = requests.get(
        "https://api.mcstatus.io/v2/status/java/5.196.4.146"
    )

    if response.status_code != 200:
        return

    data = response.json()

    online = data["online"]
    joueurs = [
        v["name_clean"]
        for v in data.get("players", {}).get("list", [])
    ]

    ctx.response(
        color= '#00FF00' if online else '#FF0000',
        description=(
            "IP : 5.196.4.146"
            + "\nVersion : 1.20.4"
            + f"\nJoueurs : {', '.join(joueurs) if joueurs else 'Aucun.'}"
        )
    )
