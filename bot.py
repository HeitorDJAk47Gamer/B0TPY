import json
import os
import random
import discord
import asyncio
import datetime
from discord.ext import commands, tasks
from discord_buttons_plugin import *
from discord.ext.commands import cooldown, BucketType, has_permissions, MissingPermissions

def get_prefix(lara, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

with open('config.json') as e:
    infos = json.load(e)
    token = infos['token']
    heitor = infos['heitor']
    ferro = infos['ferro']
    servidor = infos['servidor']

lara = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=discord.Intents.all())
buttons = ButtonsClient(lara)
lara.remove_command('help')

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

@lara.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '-'#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

@lara.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)

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

@lara.group(invoke_without_command=True)
async def adbot(ctx):
    x = discord.Embed(title=f'Adicione os bots oficiais e parceiros!')
    x.add_field(name='Flitser:', value=f'[Adicionar Flitser](https://discord.com/oauth2/authorize?client_id=754474576078962769&scope=bot&permissions=8)', inline=False)
    x.add_field(name='Glitzer:', value=f'[Adicionar Glitzer](https://discord.com/oauth2/authorize?client_id=755774575886991362&scope=bot&permissions=8)', inline=False)
    x.add_field(name='Lara BOT:', value=f'[Adicionar Lara BOT](https://discord.com/oauth2/authorize?client_id=739265612051906721&scope=bot&permissions=8)', inline=False)
    x.add_field(name='Sukhoi:', value=f'[Adicionar Sukhoi](https://discord.com/oauth2/authorize?client_id=860397194875633694&scope=bot&permissions=8)', inline=False)
    x.add_field(name=f'Saber mais:', value=f'-adbot [flitser/glitzer/lb/sukhoi]', inline=False)
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=x)

@adbot.command()
async def flitser(ctx):
    h = lara.get_user(heitor)
    fl = lara.get_user(754474576078962769)
    x = discord.Embed(title=f'Flitser')
    x.add_field(name=f'Desenvolvedor:', value=f'{h.display_name}', inline=False)
    x.add_field(name=f'Sobre:', value=f'Fliser foi desenvolvido ultimamente para música, usando código aberto!', inline=False)
    x.set_thumbnail(url=fl.avatar_url)
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=x)

@adbot.command()
async def glitzer(ctx):
    h = lara.get_user(heitor)
    gl = lara.get_user(755774575886991362)
    x = discord.Embed(title=f'Glitzer')
    x.add_field(name=f'Desenvolvedor:', value=f'{h.display_name}', inline=False)
    x.add_field(name=f'Sobre:', value=f'Quer receber atualizações dos bots desenvolvidos? Aqui está Glitzer, um bot beta dos comandos!', inline=False)
    x.set_thumbnail(url=gl.avatar_url)
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=x)

@adbot.command()
async def lb(ctx):
    h = lara.get_user(heitor)
    lr = lara.get_user(739265612051906721)
    x = discord.Embed(title=f'Lara BOT')
    x.add_field(name=f'Desenvolvedor:', value=f'{h.display_name}', inline=False)
    x.add_field(name=f'Sobre:', value=f'Lara BOT, focada em qualidade de serviços, e facilidade de acesso!\nDesenvolvida para ser pública e ajudar no gerenciamento de servidores globais.', inline=False)
    x.set_thumbnail(url=lr.avatar_url)
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.set_footer(text='O melhor para os usuários do discord!')
    x.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=x)

@adbot.command()
async def sukhoi(ctx):
    f = lara.get_user(ferro)
    sk = lara.get_user(860397194875633694)
    x = discord.Embed(title=f'Sukhoi')
    x.add_field(name=f'Desenvolvedor:', value=f'{f.display_name}', inline=False)
    x.add_field(name=f'Sobre:', value=f'Sukhoi desenvolvido para o aprendizado de programação via discord, támbem ara ajudar a facilitar de forma simples e prática.', inline=False)
    x.set_thumbnail(url=sk.avatar_url)
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.set_footer(text='Olha esses canardes de fora!')
    x.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=x)

lara.run(token)