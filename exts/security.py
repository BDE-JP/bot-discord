# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------


async def verification(message, channel):

	try: prenom, nom, identifiant = message.content.split(' ')
	except:
		prenom = nom = identifiant = None

	await message.delete()

	if not identifiant:
		return

	database.identities.add((message.author.id, prenom, nom, identifiant))

	description = (
		""
	)

	await channel.send(embed=discord.Embed(description=description))