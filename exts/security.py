# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

from ..__base__ import library_sn; discord = library_sn.discord


async def verification(message, channel):

    try: prenom, nom, identifiant = message.content.split(' ')
    except:
        prenom = nom = identifiant = None

    await message.delete()

    if not identifiant:
        return

    description = (
        f"[ ] - <@{message.author.id}>"
        + f"\n{nom.upper()} {prenom} n°{identifiant}"
    )

    await (await message.channel.send("✅")).delete(delay=30)

    msg = await channel.send(embed=discord.Embed(description=description))

    await msg.add_reaction("✅")
    await msg.add_reaction("❌")

    database.verifications.add(
        (msg.channel.id, msg.id, message.author.id, prenom, nom, identifiant)
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
            self.first_name,
            self.last_name,
            self.identifiant
        ) = data

    async def accept(self, guild):

        database.users.identity(
            (self.first_name, self.last_name, self.identifiant, self.user_id)
        )

        database.verifications.remove(self.id)

        description = (
            f"[✅] - <@{self.user_id}>"
            + f"\n{self.last_name.upper()} {self.first_name} n°{self.identifiant}"
        )

        await self.update_message(guild, description)

    async def deny(self, guild):

        database.verifications.remove(self.id)

        description = (
            f"[❌] - <@{self.user_id}>"
            + f"\n{self.last_name.upper()} {self.first_name} n°{self.identifiant}"
        )

        await self.update_message(guild, description)

    async def update_message(self, guild, description:str):

        channel = guild.get_channel(self.channel_id) 
        message = channel.get_partial_message(self.message_id)

        await message.edit(embed=discord.Embed(description=description))
        await message.clear_reactions()