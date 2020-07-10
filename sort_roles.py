#!/usr/bin/python3

from discord import Client
from functions import tuple_filter

client = Client()

@client.event
async def on_ready():
	on_ready.__code__ = (lambda:None).__code__ #delete function after first call
	guild = client.get_guild(0)
	positions, roles = zip(*filter(tuple_filter, enumerate(guild.roles)))
	roles = sorted(roles, key=lambda role: role.name, reverse=True)
	await guild.edit_role_positions(dict(zip(roles, positions)))
	await client.logout()

client.run('token', bot=False)
