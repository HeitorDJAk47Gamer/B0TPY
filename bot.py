import json
import os
import random
import discord
import asyncio
import datetime
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType, has_permissions, MissingPermissions


with open('config.json') as e:
    infos = json.load(e)
    token = infos['token']
    prefix = infos['prefix']

lara = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=discord.Intents.all())

@lara.event
async def on_ready():
    calc = lara.latency * 1000
    pong = round(calc)
    stats.start()

    print(f'Nome: {lara.user}  ID: {lara.user.id}')
    print(f'Membros Globais: {len(lara.users)}')
    print(f'Servidores Globais: {len(lara.guilds)}')
    print(f'Ping {pong} ms')

@tasks.loop(minutes=10)
async def stats():
    await lara.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{len(lara.users)} Membros'))
    await asyncio.sleep(5 * 60)
    await lara.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(lara.guilds)} Server'))

@lara.event
async def on_message(message):
    if message.author == lara.user:
        return
    elif lara.user.mentioned_in(message):
        await message.channel.send(f'Meu prefixo é: **-**')
    elif 'tu é' in message.content.lower():
        await message.channel.send(f'Não mano, tu que deixa!')

    await lara.process_commands(message)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        lara.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename[:-3]} carregado!')

@lara.command()
async def ade(ctx, pr : discord.Emoji, msg : discord.Message):
    await msg.add_reaction(pr)
    await ctx.message.delete()



@lara.command()
@commands.is_owner()
async def hab(ctx, *, command):
    command = lara.get_command(command)
    if command is None:
        await ctx.send('insira o comando!')
    elif ctx.command == command:
        ctx.send('Não pode desabilitar esse comando!')
    else:
        command.enabled = not command.enabled
        com = 'ativado' if command.enabled else 'desativado'
        await ctx.send(f'Eu tenho {com} {command.qualified_name} para você!')

lara.run(token)
