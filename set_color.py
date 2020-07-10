#!/usr/bin/python3

from discord import Client, Color
from functions import role_filter

client = Client()

def role_map(role):
	return role.name

@client.event
async def on_ready():
	on_ready.__code__ = (lambda:None).__code__ #delete function after first call
	guild = client.get_guild(0)
	member = guild.get_member_named(input('username: '))
	hex = input('color: ')
	name = '#' + hex
	color = Color(int(hex, 16))
	color_roles = map(lambda role: role.name.lower(), filter(role_filter, member.roles))
	if len(color_roles)
		if name in map(role_map, color_roles):
			await client.logout()
		else:
			for role in color_roles:
				await member.remove_roles(role)
	if name not in map(role_map, guild.roles):
		role = await guild.create_role(name = name, color = color)
	else:
		role = filter(lambda role: role.name.lower() == name , guild.roles)
	await member.add_roles(role)
	await client.logout()

client.run('token', bot=False)
