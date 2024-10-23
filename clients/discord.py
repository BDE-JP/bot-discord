# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import asyncio
import datetime

from ..__base__ import library_sn; discord = library_sn.discord
from .. import commands
from ..exts import users
from ..exts import status
from ..exts import menu_ru
from ..exts import security


intents = discord.Intents.all()


class Echecs:
    pass


class Minecraft:
    pass


class Client(discord.Client):

    def __init__(self):
        super().__init__(fetch_offline_members=False, intents=intents)

        self.manage_status_role = None 

    async def on_ready(self):

        elo_hour = None
        menu_ru_send = False

        self.guild = self.get_guild(1217518211373994014)
        self.manage_status_role = status.MangageStatusRole(self)

        while True:

            ### Menu RU

            date = datetime.datetime.utcnow()
            
            if date.hour == 8 and data.isoweekday() not in [6, 7]:
                if not menu_ru_send:
                    try: text = menu_ru.get_text()
                    except:
                        pass
                    else:
                        menu_ru_send = True
                        channel = guild.get_channel(1282350742379692042)
                        await channel.send(embed=discord.Embed(
                            description = \
                                f"_{date.strftime('%d/%m/%Y')}_ - {text}"
                        ))
            else:
                menu_ru_send = False

            ### Elo Lichess

            maj:list = users.get_new_elo() if date.hour != elo_hour else None

            if maj:
                elo_hour = date.hour
                channel = guild.get_channel(1218681676771885117)
                for user, domain, old, new in maj:
                    description = (
                        f"{'📈' if old < new else '📉'}"
                        + f" - <@{user}>: {new} ({domain})"
                    )
                    await channel.send(
                        embed = discord.Embed(description=description)
                    )

            ### Minecraft

            maj:list = users.online_minecraft()

            if maj:
                channel = guild.get_channel(1221820637837000704)
                for user, is_online in maj:
                    description = (
                        f"{user.minecraft_pseudo} s'est "
                        + f"{'connecté' if is_online else 'déconnecté'}"
                    )
                    await self.manage_status_role.update(
                        Minecraft if is_online else None,
                        guild.get_member(user.discord_id)
                    )
                    await channel.send(
                        embed = discord.Embed(description=description)
                    )
            
            ### Sleep

            await asyncio.sleep(60*10)

    async def on_presence_update(self, before, after):

        if self.manage_status_role:
            await self.manage_status_role.update(after.activity, after)

    async def on_raw_reaction_add(self, payload):

        if payload.guild_id != self.guild.id:
            return

        verification = security.get_verification_message(payload.message_id)

        if not verification:
            return

        if str(payload.emoji) == "✅":
            await verification.accept(self.guild)
        elif str(payload.emoji) == "❌":
            await verification.deny(self.guild)

    async def on_message(self, message):

        if message.author.bot:
            return

        IDENTIFICATION_CHANNEL = self.guild.get_channel(1296031913836019712)
        VERIFICATION_CHANNEL = self.guild.get_channel(1295495398542282762)

        if message.channel == IDENTIFICATION_CHANNEL:
            await security.verification(message, VERIFICATION_CHANNEL)

        await commands.get(self, message, 'discord', prefixs=['!'])
