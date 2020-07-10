#!/usr/bin/python3

from discord import Client
from functions import role_filter

client = Client()

@client.event
async def on_ready():
	on_ready.__code__ = (lambda:None).__code__ #delete function after first call
	guild = client.get_guild(0)
	memberroles = set().union(*map(lambda member: member.roles, guild.members))
	for role in set(filter(role_filter, guild.roles)) - set(filter(role_filter, memberroles)):
		print("delete {0}".format(role.name))
		await role.delete()
	await client.logout()

client.run('token', bot=False)
