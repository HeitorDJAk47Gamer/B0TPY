import json, os, random, discord, asyncio, datetime
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType, has_permissions, MissingPermissions


with open('config.json') as e:
    infos = json.load(e)
    token = infos['token']
    prefix = infos['prefix']

lara = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(prefix), case_insensitive=True, intents=discord.Intents.all())

@lara.event # evento de inicio do bot
async def on_ready():
    calc = lara.latency * 1000
    pong = round(calc)
    stats.start() # inicia todas as atividades de status

    print(f'Nome: {lara.user}  ID: {lara.user.id}')
    print(f'Membros Globais: {len(lara.users)}') #contagem membros globai
    print(f'Servidores Globais: {len(lara.guilds)}') #contagem servidores globai
    print(f'Ping {pong} ms') #ping

@tasks.loop(minutes=30)
async def stats():
    await lara.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{len(lara.users)} Membros'))
    await asyncio.sleep(15 * 60)
    await lara.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(lara.guilds)} Server'))

@lara.event #eventos simples
async def on_message(message):
    if message.author == lara.user or message.mention_everyone:
        return
    elif lara.user.mentioned_in(message):
        await message.channel.send(f'Meu prefixo é: **-**')
    await lara.process_commands(message) #pós processos de comandos

async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Wallet"] = 0
        users[str(user.id)]["Bank"] = 0

    with open("bank.json", 'w') as f:
        json.dump(users, f, indent=4)

    return True

async def get_bank_data():
    with open("bank.json", 'r') as f:
        users = json.load(f)
    return users

@lara.command()
async def balance(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["Wallet"]
    bank_amt = users[str(user.id)]["Bank"]

    em = discord.Embed(title=f"{ctx.author.name}'s balance.", color=discord.Color.teal())
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name="Bank Balance", value=bank_amt)
    await ctx.send(embed=em)

@lara.command()
@commands.cooldown(1, 24*60*60, commands.BucketType.user)
async def daily(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    earnings = random.randrange(100)
    await ctx.send(f"Você acaba de ganhar {earnings} coins")
    users[str(user.id)]["Wallet"] += earnings
    with open("bank.json", 'w') as f:
        json.dump(users, f, indent=4)


@lara.command()
async def dep(ctx, quant=0):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    wallet_amt = int(users[str(user.id)]["Wallet"])
    if wallet_amt < quant:
        await ctx.send('Saldo insuficiente!')
    else:
        await ctx.send(f"Você acaba de depositar {quant} coins")

        users[str(user.id)]["Wallet"] -= quant
        users[str(user.id)]["Bank"] += quant

        with open("bank.json", 'w') as f:
            json.dump(users, f, indent=4)
    

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        lara.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename[:-3]} carregado!')


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


lara.run(token)# rodar bot
