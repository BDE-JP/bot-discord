# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------


class MangageStatusRole:

    async def __init__(self, client):

        self.ROLE_ECOUTE = client.guild.get_role(1218643648762085488)
        self.ROLE_JOUE = client.guild.get_role(1218690409539043349)
        self.ROLE_DIFFUSE = client.guild.get_role(1219025474173272174)
        self.ROLE_ECHECS = client.guild.get_role(1218881775594373160)
        self.ROLE_MINECRAFT = client.guild.get_role(1221994436058153032)

        self.ROLES = [
            ROLE_ECOUTE, ROLE_JOUE, ROLE_DIFFUSE, ROLE_ECHECS, ROLE_MINECRAFT
        ]

    async def update(self, activity, member):

        role_added = None

        if activity:
            if isinstance(activity, (discord.Game, discord.Activity)):
                role_added = self.ROLE_JOUE
            elif isinstance(activity, discord.Spotify):
                role_added = self.ROLE_ECOUTE
            elif isinstance(activity, discord.Streaming):
                role_added = self.ROLE_DIFFUSE
            elif isinstance(activity, Echecs):
                role_added = self.ROLE_ECHECS
            elif isinstance(activity, Minecraft):
                role_added = self.ROLE_MINECRAFT

        ROLES = list(self.ROLES) # Clone

        if role_added:
            ROLES.remove(role_added)
            if role_added not in member.roles:
                await member.add_roles(role_added)

        for role in ROLES:
            if role in member.roles:
                await member.remove_roles(role)