import logging

if 0: #if True, enable debugging file
	logger = logging.getLogger('discord')
	logger.setLevel(logging.DEBUG)
	handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
	handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
	logger.addHandler(handler)
else:
	logging.basicConfig(level=logging.INFO)

import re

p = re.compile('#[0-9a-fA-F]{6}$')

def role_filter(role):
	return p.match(role.name)

def tuple_filter(tuple):
	return p.match(tuple[1].name)
