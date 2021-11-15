import json
import os
import random
import discord
import asyncio
import datetime
import requests
from discord.ext import commands, tasks
from discord_buttons_plugin import *
from discord.ext.commands import cooldown, BucketType, has_permissions, MissingPermissions


with open('config.json') as e:
    infos = json.load(e)
    token = infos['token']
    prefix = infos['prefix']

lara = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=discord.Intents.all())
buttons = ButtonsClient(lara)

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
async def conv(ctx, ids):
    x = discord.Embed(title=f'Link do bot', url=f'https://discord.com/oauth2/authorize?client_id={ids}&scope=bot&permissions=6479535680')
    await ctx.send(embed=x)


@buttons.click
async def button_one(ctx):
    await ctx.reply(f'Olá Meu camarada!')

@buttons.click
async def button_two(ctx):
    await ctx.reply('Possui 5 para experimentar!')

@buttons.click
async def button_three(ctx):
    await ctx.reply('Tome cuidado camarada!', flags = MessageFlags().EPHEMERAL)

@lara.command()
async def create(ctx):
    await buttons.send(
        content = 'Um bom exemplo de mensagem!', 
        channel = ctx.channel.id,
        components = [
            ActionRow([
                Button(
                    label='Olá', 
                    style=ButtonType().Primary, 
                    custom_id='button_one'          # Refer to line 13
                ),Button(
                    label='Nova cor',
                    style=ButtonType().Secondary,
                    custom_id='button_two'          # Refer to line 17
                )
            ]),ActionRow([
                Button(
                    label='Perigo!',
                    style=ButtonType().Danger,
                    custom_id='button_three'        # Refer to line 21
                )
            ])
        ]
    )
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


@lara.command()
async def perm(ctx, ch : discord.TextChannel, membro : discord.Member):
    perms = discord.Permissions()
    await ch.set_permissions(membro, send_messages=False)
    await ctx.send('sucesso')

@lara.command()
async def ship(ctx, ma : discord.Member, me : discord.Member):
    pp = random.randint(1, 100)
    if pp <= 20:
        texto = f'Não dará muito certo com: `{pp}%`'
    elif 20 < pp >= 50:
        texto = f'Bom... Não o resultado não foi muito ruim, mas não tenha muita esperança com: `{pp}%`'
    elif 50 < pp >= 80:
        texto = f'Opa, uma chance muito boa de ficarem juntos com: `{pp}%`'
    elif 80 < pp >= 100:
        texto = f'Olha eles, provavelmente estão juntos em segredo com: `{pp}%`'
    x = discord.Embed(title=f'Ship', description=f'{texto}\n {ma.mention}              {me.mention}')
    await ctx.send(embed=x)

@lara.command(aliases=['animes'])
async def anime(ctx,*,cat=0):
    if ctx.channel.is_nsfw():
        tipo = 'nsfw'
        x = ['waifu','neko','trap','blowjob']
    else:
        tipo = 'sfw'
        x = ['waifu','neko','shinobu','megumin','bully','cuddle','cry','hug','awoo','kiss','lick','pat','smug','bonk','yeet','blush','smile','wave','highfive','handhold','nom','bite','glomp','slap','kill','kick','happy','wink','poke','dance','cringe']
    if cat == 0:
        cat = random.choice(x)
    r = requests.get(f'https://api.waifu.pics/{tipo}/{cat}')
    r = str(r.text)
    r = json.loads(str(r))
    await ctx.send(r['url'])


@lara.command(aliases=['beijar'])
async def kiss(ctx, membro : discord.Member):
    r = requests.get(f'https://nekos.life/api/v2/img/kiss')
    r = str(r.text)
    r = json.loads(str(r))
    x = discord.Embed(title='Beijinho!', description=f'{ctx.author.mention} beijou {membro.mention}')
    x.set_image(url=r['url'])
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=x)
    await msg.add_reaction('❤')

@lara.command(aliases=['abraçar'])
async def hug(ctx, membro : discord.Member):
    r = requests.get(f'https://nekos.life/api/v2/img/hug')
    r = str(r.text)
    r = json.loads(str(r))
    x = discord.Embed(title='Abraçooo!', description=f'{ctx.author.mention} abraçou {membro.mention}')
    x.set_image(url=r['url'])
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=x)
    await msg.add_reaction('❤')

@lara.command(aliases=['tapa'])
async def slap(ctx, membro : discord.Member):
    r = requests.get(f'https://nekos.life/api/v2/img/slap')
    r = str(r.text)
    r = json.loads(str(r))
    x = discord.Embed(title='Tapão!', description=f'{ctx.author.mention} deu um tapão em {membro.mention}')
    x.set_image(url=r['url'])
    x.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=x)

lara.run(token)
