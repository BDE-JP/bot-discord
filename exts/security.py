# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

from ..__base__ import library_sn; discord = library_sn.discord

from .. import database


async def send_message_confirm(channel, author_id, nom, prenom, identifiant):

    description = (
        f"`[⌛]` - <@{author_id}>"
        + f"\n{nom} {prenom} n°{identifiant}"
    )

    msg = await channel.send(embed=discord.Embed(description=description))

    await msg.add_reaction("✅")
    await msg.add_reaction("❌")

    database.verifications.add(
        (msg.channel.id, msg.id, author_id, nom, prenom, identifiant)
    )


def get_verification_message(message_id:int):

    data = database.verifications.get_with_message(message_id).fetchone()

    if data:
        return Verification(data)


class Verification:

    def __init__(self, data:tuple):

        (
            self.id,
            self.channel_id,
            self.message_id,
            self.user_id,
            self.last_name,
            self.first_name,
            self.identifiant
        ) = data

    async def accept(self, guild):

        database.users.identity(
            (self.last_name, self.first_name, self.identifiant, self.user_id)
        )

        database.verifications.remove(self.id)

        description = (
            f"`[✅]` - <@{self.user_id}>"
            + f"\n{self.last_name} {self.first_name} n°{self.identifiant}"
        )

        member = guild.get_member(self.user_id)
        role_EXISTE = guild.get_role(1218642619614105740)

        if role_EXISTE not in member.roles:
            await member.add_roles(role_EXISTE)

        await self.update_message(guild, description)

    async def deny(self, guild):

        database.verifications.remove(self.id)

        description = (
            f"`[❌]` - <@{self.user_id}>"
            + f"\n{self.last_name} {self.first_name} n°{self.identifiant}"
        )

        await self.update_message(guild, description)

    async def update_message(self, guild, description:str):

        channel = guild.get_channel(self.channel_id)

        if not channel:
            return

        message = channel.get_partial_message(self.message_id)

        if not message:
            return

        await message.edit(embed=discord.Embed(description=description))
        await message.clear_reactions()
