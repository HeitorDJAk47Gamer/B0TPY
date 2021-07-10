import json
import asyncio
import discord
from discord.ext import commands
import random
import datetime


with open('config.json') as e:
  infos = json.load(e)
  token = infos['token']
  prefixo = infos['prefix']
  heitor = infos['heitor']
  tess = infos['tess']
  ikki = infos['ikki']
  chsug = infos['chsug']
  chfeed = infos['chfeed']

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

@lara.group(invoke_without_command=True, aliases=['ajuda', 'helper'])
async def help(ctx):
  x = discord.Embed(title='Lista de comandos:', description=f'Use {prefixo}help (comando) para obter mais informações!')
  x.add_field(name='Diversão', value='Dado, hug, Anime, D&D, Moeda')
  x.add_field(name='Utilidades', value='Bot, Server, User, Ping, Membros, Say, Code, Report')
  x.add_field(name='Moderação', value='Ban, Kick, Cargo')
  await ctx.send(embed=x)

@help.command()
async def kick(ctx):
  x = discord.Embed(title='Expulsar', description='**Moderação**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[kick, expulsar]', inline=False)
  x.add_field(name='Descrição:', value='Comando para expulsar um membro do servidor.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def ban(ctx):
  x = discord.Embed(title='Banir', description='**Moderação**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[ban, banir]', inline=False)
  x.add_field(name='Descrição:', value='Comando para banir um membro do servidor.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def cargo(ctx):
  x = discord.Embed(title='Cargo', description='**Moderação**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[cargo]', inline=False)
  x.add_field(name='Descrição:', value='Comando para adicionar uma cargo a um determinado membro.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def anime(ctx):
  x = discord.Embed(title='Anime', description='**Diversão**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[anime]', inline=False)
  x.add_field(name='Descrição:', value='Uma imagem de anime aleatória.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def dado(ctx):
  x = discord.Embed(title='Dado', description='**Diversão**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[dado]', inline=False)
  x.add_field(name='Descrição:', value='Para rolar um dado ou mais dados com modificardores (- ou +), de qualquer valor.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def moeda(ctx):
  x = discord.Embed(title='Moeda', description='**Diversão**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[moeda, cara, coroa]', inline=False)
  x.add_field(name='Descrição:', value='Comando de cara ou coroa.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def dnd(ctx):
  x = discord.Embed(title='D&D', description='**Diversão**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[dnd, d&d]', inline=False)
  x.add_field(name='Descrição:', value='Comando para ajudar jogadores de Dungeons & Dragons.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def hug(ctx):
  x = discord.Embed(title='', description='**Diversão**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[abraçar, hug]', inline=False)
  x.add_field(name='Descrição:', value='Dê um abraço em alguém.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def bot(ctx):
  x = discord.Embed(title='Bot', description='**Utilidades**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[bot]', inline=False)
  x.add_field(name='Descrição:', value='Comando para exibir informações do bot.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def server(ctx):
  x = discord.Embed(title='Server', description='**Utilidades**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[server]', inline=False)
  x.add_field(name='Descrição:', value='Comando para exibir informações do servidor.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def user(ctx):
  x = discord.Embed(title='', description='**Utilidades**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[user]', inline=False)
  x.add_field(name='Descrição:', value='Comando para exibir informações do usuário citado.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def ping(ctx):
  x = discord.Embed(title='Ping', description='**Utilidades**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[ping]', inline=False)
  x.add_field(name='Descrição:', value='Mostrar latência atual do bot.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def membros(ctx):
  x = discord.Embed(title='', description='**Utilidades**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[membros]', inline=False)
  x.add_field(name='Descrição:', value='Membros totais no servidor.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def say(ctx):
  x = discord.Embed(title='', description='**Utilidades**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[ban, banir]', inline=False)
  x.add_field(name='Descrição:', value='Repetir o que foi digitado no comando.', inline=False)
  await ctx.send(embed=x)

@help.command()
async def code(ctx):
  x = discord.Embed(title='Code', description='**Utilidades**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[code]', inline=False)
  x.add_field(name='Descrição:', value='Formate seu código instantaneamente', inline=False)
  await ctx.send(embed=x)

@help.command()
async def report(ctx):
  x = discord.Embed(title='Reportar', description='**Utilidades**')
  x.add_field(name='Sintaxe:', value=f'{prefixo}[report, reportar]', inline=False)
  x.add_field(name='Descrição:', value='Para reportar erros ou bugs do bot para a equipe.', inline=False)
  await ctx.send(embed=x)


@lara.command()
async def ping(ctx):
  calc = bot.latency * 1000
  pong = round(calc)
  await ctx.message.delete()

  x = discord.Embed(title='**Pong**', description=f'{pong} `ms`', color=0xff0000)

  y = discord.Embed(title='**Pong**', description=f'{pong} `ms`', color=0xffff00)

  z = discord.Embed(title='**Pong**', description=f'{pong} `ms`', color=0x008000)

  if pong > 160:
    msg = await ctx.send(embed=x)
    await msg.add_reaction('🏓')
  elif 80 <= pong <= 160:
    msg = await ctx.send(embed=y)
    await msg.add_reaction('🏓')
  elif pong < 80:
    msg = await ctx.send(embed=z)
    await msg.add_reaction('🏓')

@lara.command()
async def dado(ctx, numero=0, h='nada', mod=0, d=1):
  r = []
  while 0 < d:
      r.append(random.randint(1, numero))
      d = (d - 1)
  total = sum(r)
  y = discord.Embed(title='Dados', description='🎲 Rolando dado...')
  if numero != 0 and h == 'nada':
    x = discord.Embed(title=f'**D{numero}**', description=f'{r} = {total}')
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=y)
    await asyncio.sleep(0.7)
    await msg.edit(embed=x)
    await msg.add_reaction('🎲')
  elif numero != 0 and h == '-':
    sub = (total - mod)
    x = discord.Embed(title=f'**D{numero}**', description=f'{r} + {mod} = {sub}')
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=y)
    await asyncio.sleep(0.7)
    await msg.edit(embed=x)
    await msg.add_reaction('🎲')
  elif numero != 0 and h == '+':
    soma = (total + mod)
    x = discord.Embed(title=f'**D{numero}**', description=f'{r} + {mod}  = {soma}')
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=y)
    await asyncio.sleep(0.7)
    await msg.edit(embed=x)
    await msg.add_reaction('🎲')
  else:
     await ctx.reply('**Você precisa definir um número máximo!**')


@lara.command(name='cara ou coroa', aliases=['cara', 'coroa'], help='Jogue cara ou coroa!')
async def moeda(ctx):

  var = random.randint(1, 2)
  if var == 1:  # cara
    msg = await ctx.send('Deu cara!')
    await msg.add_reaction('😀')
  elif var == 2:  # coroa
    msg = await ctx.send('Deu coroa!')
    await msg.add_reaction('👑')


@lara.command(name='developer', help='Você é o developer?')
async def dev(ctx):
  if ctx.author.id == heitor:
    await ctx.send('Você é o desenvolvedor!')
  else:
    await ctx.send('Você não é o desenvolvedor!')


@lara.command(name='Tess')
async def T(ctx):
  x = discord.Embed(title='**TESS-CHAN**', description=f'Você é uma pessoa incrível, realmente sou muito sortudo por ter você como amiga!')
  x.timestamp = datetime.datetime.utcnow()
  if ctx.author.id == tess:
    msg = await ctx.channel.send(embed=x)
    await msg.add_reaction('❤')
    await msg.add_reaction('😃')
  else:
    msg = await ctx.send('Você não é a Tess!')
    await msg.add_reaction('😒')


@lara.command(name='animes')
async def anime(ctx):
  img = random.randint(1, 200)
  await ctx.send(f'https://larab0tbeta.heitordjak47.repl.co/galeria/{img}.jpg')


@lara.command(name='repetir')
async def say(ctx, *, message):
  try:
    await ctx.send(message)
    await ctx.message.delete()
  except:
    await ctx.send('Por favor, dê alguma mensagem!')


@lara.command(name='code', description='Pra usar este comando: coloque a extensão da linguagem, depois faça uma quebra de linha e insira o código')
async def code(ctx, prog=None, *, code):
  user = ctx.message.author.display_name
  try:
    await ctx.send(f'**código de:** `{user}` ```{prog}\n{code}\n```')
    await ctx.message.delete()
  except:
    await ctx.send('Por favor, insira o código!')


@lara.command(name='oloko')
async def rolada_no_heitor(ctx):
  msg = await ctx.send('Rolada nele!')
  await msg.add_reaction('😒')


@lara.command(name='loja')
async def loja(ctx):
  y = discord.Embed(title='**Loja!**', description='Abrindo a loja...')
  #
  x = discord.Embed(title='**Loja!**', description='itens da loja Lara: use: !comprar (nome do item) para comprar!')
  x.add_field(name='📱**Celular:**', value='`1000$`', inline=True)
  x.add_field(name='💻 **PC:**', value='`5000$`', inline=True)
  x.add_field(name='⛏ **Picareta:**', value='`20$`', inline=True)
  x.add_field(name='⛏ **10x Picaretas:**', value='~~`200$`~~ => `180$`', inline=True)
  x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  x.timestamp = datetime.datetime.utcnow()
  msg = await ctx.send(embed=y)
  await asyncio.sleep(0.3)
  await msg.edit(embed=x)
  await msg.add_reaction('💵')


@lara.command()
async def kick(ctx, membro : discord.Member, *, motivo=None):
  x = discord.Embed(title='**Expulsão**')
  x.add_field(name='*Membro Expulso:*', value=f'{membro.mention}', inline=True)
  x.add_field(name='*Por:*', value=f'{ctx.author.mention}', inline=True)
  x.add_field(name='*Motivo:*', value=f'{motivo}', inline=False)
  x.timestamp = datetime.datetime.utcnow()
  await membro.kick()
  await ctx.send(embed=x)


@lara.command()
async def ban(ctx, membro : discord.Member, *, motivo=None):
  x = discord.Embed(title='**Expulsão**')
  x.add_field(name='*Membro Banido:*', value=f'{membro.mention}', inline=True)
  x.add_field(name='*Por:*', value=f'{ctx.author.mention}', inline=True)
  x.add_field(name='*Motivo:*', value=f'{motivo}', inline=False)
  x.timestamp = datetime.datetime.utcnow()
  await membro.ban()
  await ctx.send(embed=x)


@lara.command(aliases=['d&d'])
async def dnd(ctx, comando=0):
  if comando == 0:
    z = '```'
    x = discord.Embed(title='**Comandos de D&D:**')
    x.add_field(name='*Compra de Ponto:*', value=f'{z}\n{prefixo}D&D 1\n{z}', inline=False)
    x.add_field(name='*Modificadores:*', value=f'{z}\n{prefixo}D&D 2\n{z}', inline=False)
    x.add_field(name='*Pré-definição de pontos:*', value=f'{z}\n{prefixo}D&D 3\n{z}', inline=False)
    x.add_field(name='*CD:*', value=f'{z}\n{prefixo}D&D 4\n{z}', inline=False)
    x.add_field(name='*Ficha:*', value=f'{z}\n{prefixo}D&D 5\n{z}', inline=False)
    x.add_field(name='*Ouro:*', value=f'{z}\n{prefixo}D&D 6\n{z}', inline=False)
    x.add_field(name='*Pacotes:*', value=f'{z}\n{prefixo}D&D 7\n{z}', inline=False)
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=x)
  
  elif comando == 1:
    x = discord.Embed(title='**Compra de Pontos**')
    x.set_image(url='https://cdn.discordapp.com/attachments/753004109790969867/853721835899715604/cp.png')
    await ctx.send(embed=x)

  elif comando == 2:
    x = discord.Embed(title='**Modificadores**')
    x.set_image(url='https://cdn.discordapp.com/attachments/753004109790969867/853721845420261386/mod.png')
    await ctx.send(embed=x)

  elif comando == 3:
    x = discord.Embed(title='**Distribuição de pontos pré-Definida**')
    x.add_field(name='*Você pode usar os seguintes valores:*', value='15, 14, 13, 12, 10, 8.', inline=False)
    x.add_field(name='*Diatribua esses valores entre:*', value='**Força, Destreza, Constituição, Inteligência, Sabedoria, Carisma**', inline=False)
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=x)

  elif comando == 4:
    d = discord.Embed(title='**CD**')
    d.set_image(url='https://cdn.discordapp.com/attachments/753004109790969867/853721828162011146/cd.png')
    await ctx.send(embed=d)

  elif comando == 5:
    x = discord.Embed(title='**Ficha**', url='https://cdn.discordapp.com/attachments/753004109790969867/853721843785531422/dd-5e-ficha-de-personagem-automatica-biblioteca-elfica.pdf', description='Clique para baixar a ficha D&De5 em Português BR automática.')
    await ctx.send(embed=x)

  elif comando == 6:
    x = discord.Embed(title='**Ouro Inicial**')
    x.set_image(url='https://cdn.discordapp.com/attachments/753004109790969867/853721847496966204/ouro.jpg')
    await ctx.send(embed=x)

  elif comando == 7 :
    x = discord.Embed(title='**Pacotes**')
    x.set_image(url='https://cdn.discordapp.com/attachments/753004109790969867/853721851348123698/pct.png')
    await ctx.send(embed=x)


@lara.command()
async def cargo(ctx, user : discord.Member, cargo : discord.Role):
  await user.add_roles(cargo)
  x = discord.Embed(title='Cargo adicionado!')
  x.add_field(name='**Membro:**', value=user.mention, inline=False)
  x.add_field(name='*Cargo adicionado:*', value=cargo.mention, inline=False)
  x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  x.timestamp = datetime.datetime.utcnow()
  x.set_thumbnail(url=ctx.guild.icon_url)
  msg = await ctx.send(embed=x)
  await msg.add_reaction('✅')


@lara.command(alises=['usuario', 'u'])
async def user(ctx, membro : discord.Member = 'nada'):
  if membro != 'nada':
    x = discord.Embed(title='**Informações:**')
    x.add_field(name='Nome:', value=membro.display_name, inline=False)
    x.add_field(name='ID:', value=membro.id, inline=False)
    x.add_field(name='Criado em:', value=membro.created_at.strftime('Data: %d/%m/%Y Hora: %H:%M:%S %p'), inline=False)
    x.set_thumbnail(url=membro.avatar_url)
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=x)
  else:
    x = discord.Embed(title='**Informações:**')
    x.add_field(name='Nome:', value=ctx.author.display_name, inline=False)
    x.add_field(name='ID:', value=ctx.author.id, inline=False)
    x.add_field(name='Criado em:', value=ctx.guild.created_at.strftime('Data: %d/%m/%Y Hora: %H:%M:%S %p'), inline=False)
    x.set_thumbnail(url=ctx.author.avatar_url)
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=x)


@lara.command()
async def server(ctx):
  membros = len(ctx.guild.members)
  cargos = len(ctx.guild.roles)
  x = discord.Embed(title='**Informações:**')
  x.add_field(name='Nome:', value=ctx.guild.name, inline=False)
  x.add_field(name='ID:', value=ctx.guild.id, inline=False)
  x.add_field(name='Dono:', value=ctx.guild.owner.mention, inline=False)
  x.add_field(name='Criado em:', value=ctx.guild.created_at.strftime('Data: %d/%m/%Y Hora: %H:%M:%S %p'), inline=False)
  x.add_field(name='Região:', value=ctx.guild.region, inline=False)
  x.add_field(name='Membros:', value=f'`{membros}`', inline=False)
  x.add_field(name=f'Cargos:', value=f'`{cargos}`', inline=False)
  x.set_thumbnail(url=ctx.guild.icon_url)
  x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  x.timestamp = datetime.datetime.utcnow()
  await ctx.send(embed=x)


@lara.command()
async def report(ctx, *, report=None):
  z = discord.Embed(title='Novo Erro!', description='Carregando o report...')
  canal = lara.get_channel(754741603230416896)
  x = discord.Embed(title='**Report de Erro!**')
  x.add_field(name='Server:', value=ctx.guild.name, inline=False)
  x.add_field(name='ID do Server:', value=ctx.guild.id, inline=False)
  x.add_field(name='Relatório:', value=report, inline=False)
  x.set_thumbnail(url=ctx.guild.icon_url)
  x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  x.timestamp = datetime.datetime.utcnow()
  msg = await canal.send(embed=z)
  await asyncio.sleep(0.8)
  await msg.edit(embed=x)
  #Developer
  await ctx.message.add_reaction('✅')
  #reação
  y = discord.Embed(title='#Equipe Lara B0T')
  y.add_field(name=f'**Olá {ctx.author.display_name}**', value='*Agradecemos pela sua colaboração com nosso projeto, iremos analisar o problema e solucioná-lo!*')
  y.timestamp = datetime.datetime.utcnow()
  await ctx.author.send(embed=y)


@lara.command()
async def reportar(ctx, *, text=None):
  z = discord.Embed(title='Novo Erro!', description='Carregando o report...')
  dm = lara.get_user(heitor)
  x = discord.Embed(title='**Report de Erro!**')
  x.add_field(name='Server:', value=ctx.guild.name, inline=False)
  x.add_field(name='ID do Server:', value=ctx.guild.id, inline=False)
  x.add_field(name='Relatório:', value=text, inline=False)
  x.set_thumbnail(url=ctx.guild.icon_url)
  x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  x.timestamp = datetime.datetime.utcnow()
  msg = await dm.send(embed=z)
  await asyncio.sleep(1.0)
  await msg.edit(embed=x)
  #Developer
  await ctx.message.add_reaction('✅')
  #reação
  y = discord.Embed(title='#Equipe Lara B0T')
  y.add_field(name=f'**Olá {ctx.author.display_name}**', value='*Agradecemos pela sua colaboração com nosso projeto, iremos analisar o problema e solucioná-lo!*')
  y.timestamp = datetime.datetime.utcnow()
  await ctx.author.send(embed=y)


@lara.command(aliases=['team', 'lara', 'eq'])
async def equipe(ctx):
  y = discord.Embed(title='Equipe Lara', description='*Verificando*...')
  if ctx.author.id == heitor:
    x = discord.Embed(title='Olá Heitor!', description='*Opa olá meu caro criador e desenvolvedor. Gostaria de ouvir um Lo-Fi?*')
    x.set_thumbnail(url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=y)
    await asyncio.sleep(1.0)
    await msg.edit(embed=x)
    await msg.add_reaction('✅')
  elif ctx.author.id == tess:
    x = discord.Embed(title='Opa Tess!', description='*Oiiiii Tess, sua fofa querida. Que tal jogar um Mine, ouvir Addict?*')
    x.set_thumbnail(url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=y)
    await asyncio.sleep(1.0)
    await msg.edit(embed=x)
    await msg.add_reaction('✅')
  elif ctx.author.id == ikki:
    x = discord.Embed(title='Olá Ikki!', description='*Fala ~~ikkigay~~ IkkiArtz, tenho uma pergunta importante...* \n**Tu é mano?**')
    x.set_thumbnail(url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=y)
    await asyncio.sleep(1.0)
    await msg.edit(embed=x)
    await msg.add_reaction('✅')
  else:
    msg = await ctx.send(embed=y)
    await asyncio.sleep(1.0)
    await msg.edit(f'Olá {ctx.author.display_name}, esse comando está reservado apenas para membros da Equipe!')


@lara.command()
async def clear(ctx, n=0):
  if n <= 0:
    await ctx.send('Você precisa digitar a quantidade de menssagens para serem deletadas')
  else:
    await ctx.channel.purge(limit=int(n))
    x = discord.Embed(title='Sistema de Limpar!')
    x.add_field(name='Menssagens deletadas:', value=f'{n}')
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=x)


@lara.command(alises=['foto', 'img'])
async def avatar(ctx, membro : discord.Member = 'nada'):
  if membro != 'nada':
    x = discord.Embed(title=f'Avatar de {membro.display_name}')
    x.set_image(url=membro.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=x)
  else:
    x = discord.Embed(title='Seu avatar')
    x.set_image(url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=x)


@lara.command()
async def bot(ctx):
  calc = lara.latency * 1000
  pong = round(calc)
  a = lara.get_user(heitor)
  b = lara.get_user(tess)
  c = lara.get_user(ikki)
  x = discord.Embed(title='Bot Info:')
  x.add_field(name='Nome:', value=lara.user.display_name, inline=True)
  x.add_field(name='ID:', value=lara.user.id, inline=True)
  x.add_field(name='Ping:', value=f'`{pong}`', inline=True)
  x.add_field(name='Criado em:', value=lara.user.created_at.strftime('Data: %d/%m/%Y Hora: %H:%M:%S %p'), inline=True)
  x.add_field(name='criador:', value=a.display_name, inline=False)
  x.add_field(name='Equipe:', value=f'{b.display_name} e {c.display_name}', inline=False)
  x.set_thumbnail(url=user.avatar_url)
  x.timestamp = datetime.datetime.utcnow()
  msg = await ctx.send(embed=x)
  await msg.add_reaction('<:LaraBoT:773736694733996062>')


@lara.command()
async def membros(ctx):
  mb = len(ctx.guild.members)
  await ctx.send(f'Este servidor possui: {mb} membros')


@lara.command(aliases=['contribuir', 'sugestao'])
async def sug(ctx, *, message):
  canal = lara.get_channel(chsug)
  x = discord.Embed(title='Nova sugestão')
  x.add_field(name='Membro:', value=ctx.author, inline=False)
  x.add_field(name='`Sugerido:`', value=message, inline=False)
  x.timestamp = datetime.datetime.utcnow()
  await canal.send(embed=x)
  await ctx.message.add_reaction('✅')


@lara.command(aliases=['feedback', 'fb'])
async def feed(ctx, *, message):
  canal = lara.get_channel(chfeed)
  x = discord.Embed(title='Nova FeedBack')
  x.add_field(name='Membro:', value=ctx.author, inline=False)
  x.add_field(name='`FeedBack:`', value=message, inline=False)
  x.timestamp = datetime.datetime.utcnow()
  await canal.send(embed=x)
  await ctx.message.add_reaction('✅')


@lara.command()
async def hug(ctx, membro : discord.Member):
  x = discord.Embed(title='Abraçooo!', description=f'{ctx.author.mention} abraçou {membro.mention}')
  x.set_image(url='https://larab0tbeta.heitordjak47.repl.co/galeria/1.jpg')
  x.timestamp = datetime.datetime.utcnow()
  msg = await ctx.channel.send(embed=x)
  await msg.add_reaction('❤')

lara.run(token)