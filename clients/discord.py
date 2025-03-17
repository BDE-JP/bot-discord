# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import asyncio
import datetime
import logging
import traceback

from ..__base__ import manage
from ..__base__ import library_sn; discord = library_sn.discord
from .. import commands
from ..exts import musics
from ..exts import users
from ..exts import status
from ..exts import menu_ru
from ..exts import security
from ..exts import adherents

logger = logging.getLogger(__name__)

intents = discord.Intents.all()


class Client(discord.Client):

    def __init__(self):
        super().__init__(fetch_offline_members=False, intents=intents)

        self.manage_status_role = None 

    async def on_ready(self):

        print("BOt BDE-JP login !")

        self.manage_slash_commands = manage.slash_commands.ManagerSlashCommands(
            self.bot__.data.params["application_id"],
            self.bot__.data.params["token"]
        )

        for module in commands.modules.values():
            await self.manage_slash_commands.register_application_commands(
                module.commands
            )

        elo_hour = None
        menu_ru_send = False
        music_send = False

        self.guild = self.get_guild(1217518211373994014)
        self.manage_status_role = status.MangageStatusRole(self)

        while True:

            ### Menu RU

            date = datetime.datetime.utcnow()

            if date.hour == 9 and date.isoweekday() not in [6, 7]:
                if not menu_ru_send:
                    try: text = menu_ru.get_text()
                    except:
                        logger.error(traceback.format_exc())
                    else:
                        menu_ru_send = True
                        channel = self.guild.get_channel(1334677225445785610)
                        await channel.send(embed=discord.Embed(
                            description = \
                                f"_{date.strftime('%d/%m/%Y')}_ - {text}"
                        ))
            else:
                menu_ru_send = False

            ### Musique du jour

            if date.hour == 23:
                if not music_send:
                    try: embed = musics.today()
                    except:
                        logger.error(traceback.format_exc())
                    else:
                        music_send = True
                        channel = self.guild.get_channel(1347698675257704498)
                        msg = await channel.send(embed=embed)
                        await msg.add_reaction("🤍")
            else:
                music_send = False

            ### Elo Lichess

            maj:list = None # users.get_new_elo() if date.hour != elo_hour else None

            if maj:
                elo_hour = date.hour
                channel = self.guild.get_channel(1218681676771885117)
                for user, domain, old, new in maj:
                    description = (
                        f"{'📈' if old < new else '📉'}"
                        + f" - <@{user}>: {new} ({domain})"
                    )
                    await channel.send(
                        embed = discord.Embed(description=description)
                    )

            ### Minecraft

            maj:list = None # users.online_minecraft()

            if maj:
                channel = self.guild.get_channel(1221820637837000704)
                for user, is_online in maj:
                    description = (
                        f"{user.minecraft_pseudo} s'est "
                        + f"{'connecté' if is_online else 'déconnecté'}"
                    )
                    await self.manage_status_role.update(
                        status.Minecraft() if is_online else None,
                        guild.get_member(user.discord_id)
                    )
                    await channel.send(
                        embed = discord.Embed(description=description)
                    )
            
            ### Sleep

            await asyncio.sleep(60*10)

    async def on_presence_update(self, before, after):

        if self.manage_status_role:
            activity = status.sort_activities(after.activities or [None])[0]
            await self.manage_status_role.update(activity, after)

        if isinstance(before.activity, discord.Spotify):
            musics.add_music(before, before.activity)

        await adherents.update(after)

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

    async def on_interaction(self, interaction: discord.Interaction):

        if interaction.type == discord.InteractionType.application_command:
            await commands.get(self, 'discord', interaction=interaction)

    async def on_message(self, message):

        if message.author.bot:
            return

        await commands.get(self, "discord", message=message, prefixs=['!'])
