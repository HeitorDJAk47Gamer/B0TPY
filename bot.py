import json
import sys
import os
import random
import discord
from discord.ext import commands

with open('config.json') as e:
    infos = json.load(e)
    token = infos['token']
    prefixo = infos['prefix']

lara = commands.Bot(command_prefix=prefixo, case_insensitive=True, intents=discord.Intents.all())
lara.remove_command('help')

@lara.event
async def on_ready():
    calc = lara.latency * 1000
    pong = round(calc)

    await lara.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Discord.PY'))
    print(f'Nome: {lara.user}  ID: {lara.user.id}')
    print(f'Membros Globais: {len(lara.users)}')
    print(f'Servidores Globais: {len(lara.guilds)}')
    print(f'Ping {pong} ms')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        lara.load_extension(f'cogs.{filename[:-3]}')

lara.run(token)