#!/usr/bin/python3

from discord import Client
from functions import role_filter

client = Client()

@client.event
async def on_ready():
	on_ready.__code__ = (lambda:None).__code__ #delete function after first call
	guild = client.get_guild(0)
	for role in filter(lambda role: role_filter(role) and role.name != role.name.lower(), guild.roles):
		print("normalize {0}".format(role.name))
		await role.edit(name=role.name.lower())
	await client.logout()

client.run('token', bot=False)
