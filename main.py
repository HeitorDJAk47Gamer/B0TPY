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
  lara = infos['lara']

bot = commands.Bot(command_prefix=prefixo,case_insensitive=True, intents=discord.Intents.all())


@bot.event
async def on_ready():
  calc = bot.latency * 1000
  pong = round(calc)

  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Discord.PY'))
  print(f'Nome: {bot.user}  ID: {bot.user.id}')
  print(f'Membros Globais: {len(bot.users)}')
  print(f'Servidores Globais: {len(bot.guilds)}')
  print(f'Ping {pong} ms')

@bot.command()
async def ola(ctx):
  await ctx.send(f'Olá, {ctx.author.display_name}')


@bot.command()
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

@bot.command()
async def dado(ctx, numero=0, h='nada', mod=0):
  y = discord.Embed(title='Dados', description='🎲 Rolando dado...')
  if numero != 0 and h == 'nada':
    var = random.randint(1, int(numero))
    x = discord.Embed(title=f'**D{numero}**', description=f'{var}')
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=y)
    await asyncio.sleep(0.7)
    await msg.edit(embed=x)
    await msg.add_reaction('🎲')
  elif numero != 0 and h == '-':
    var = random.randint(1, int(numero))
    sub = (var - mod)
    x = discord.Embed(title=f'**D{numero}**', description=f'{var} - {mod} = {sub}')
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=y)
    await asyncio.sleep(0.7)
    await msg.edit(embed=x)
    await msg.add_reaction('🎲')
  elif numero != 0 and h == '+':
    var = random.randint(1, int(numero))
    soma = (var + mod)
    x = discord.Embed(title=f'**D{numero}**', description=f'{var} + {mod} = {soma}')
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=y)
    await asyncio.sleep(0.7)
    await msg.edit(embed=x)
    await msg.add_reaction('🎲')
  else:
     await ctx.reply('**Você precisa definir um número máximo!**')


@bot.command(name='cara ou coroa', aliases=['cara', 'coroa'], help='Jogue cara ou coroa!')
async def moeda(ctx):

  var = random.randint(1, 2)
  if var == 1:  # cara
    msg = await ctx.send('Deu cara!')
    await msg.add_reaction('😀')
  elif var == 2:  # coroa
    msg = await ctx.send('Deu coroa!')
    await msg.add_reaction('👑')


@bot.command(name='ddq')
async def desq(ctx, numero):
  a = int(numero)
  if a == 8:
    await ctx.send('Acertou!')
  elif a != 8:
    await ctx.send('Errou!')


@bot.command(name='developer', help='Você é o developer?')
async def dev(ctx):
  if ctx.author.id == heitor:
    await ctx.send('Você é o desenvolvedor!')
  else:
    await ctx.send('Você não é o desenvolvedor!')


@bot.command(name='sugestão')
async def sug(ctx, *, message=None):
  if message != None:
    x = discord.Embed(title='SUGESTÃO', description=f'{message}', color=0x000000)
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.channel.send(embed=x)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')
  else:
    await ctx.reply('**Dê sua sugestão!**')



@bot.command(name='Tess')
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


@bot.command(name='animes')
async def anime(ctx):
  img = random.randint(1, 200)
  await ctx.send(f'https://larab0tbeta.heitordjak47.repl.co/galeria/{img}.jpg')


@bot.command(name='repetir')
async def say(ctx, *, message):
  try:
    await ctx.send(message)
    await ctx.message.delete()
  except:
    await ctx.send('Por favor, dê alguma mensagem!')


@bot.command(name='code', description='Pra usar este comando: coloque a extensão da linguagem, depois faça uma quebra de linha e insira o código')
async def code(ctx, prog=None, *, code):
  user = ctx.message.author.display_name
  try:
    await ctx.send(f'**código de:** `{user}` ```{prog}\n{code}\n```')
    await ctx.message.delete()
  except:
    await ctx.send('Por favor, insira o código!')


@bot.command(name='oloko')
async def rolada_no_heitor(ctx):
  msg = await ctx.send('Rolada nele!')
  await msg.add_reaction('😒')


@bot.command(name='loja')
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


@bot.command()
async def kick(ctx, membro : discord.Member, *, motivo=None):
  x = discord.Embed(title='**Expulsão**')
  x.add_field(name='*Membro Expulso:*', value=f'{membro.mention}', inline=True)
  x.add_field(name='*Por:*', value=f'{ctx.author.mention}', inline=True)
  x.add_field(name='*Motivo:*', value=f'{motivo}', inline=False)
  x.timestamp = datetime.datetime.utcnow()
  await membro.kick()
  await ctx.send(embed=x)


@bot.command()
async def ban(ctx, membro : discord.Member, *, motivo=None):
  x = discord.Embed(title='**Expulsão**')
  x.add_field(name='*Membro Banido:*', value=f'{membro.mention}', inline=True)
  x.add_field(name='*Por:*', value=f'{ctx.author.mention}', inline=True)
  x.add_field(name='*Motivo:*', value=f'{motivo}', inline=False)
  x.timestamp = datetime.datetime.utcnow()
  await membro.ban()
  await ctx.send(embed=x)


@bot.command(aliases=['d&d'])
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


@bot.command()
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


@bot.command(alises=['usuario', 'u'])
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


@bot.command()
async def server(ctx):
  membros = len(ctx.guild.members)
  cargos = len(ctx.guild.roles)
  x = discord.Embed(title='**Informações:**')
  x.add_field(name='Nome:', value=ctx.guild.name, inline=False)
  x.add_field(name='ID:', value=ctx.guild.id, inline=False)
  x.add_field(name='Dono:', value=ctx.guild.owner.mention, inline=False)
  x.add_field(name='Criado em:', value=ctx.guild.created_at.strftime('Data: %d/%m/%Y Hora: %H:%M:%S %p'), inline=False)
  x.add_field(name='Região:', value=ctx.guild.region, inline=False)
  x.add_field(name='Membros:', value=membros, inline=False)
  x.add_field(name=f'Cargos:', value=cargo, inline=False)
  x.set_thumbnail(url=ctx.guild.icon_url)
  x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  x.timestamp = datetime.datetime.utcnow()
  await ctx.send(embed=x)


@bot.command()
async def report(ctx, *, report=None):
  z = discord.Embed(title='Novo Erro!', description='Carregando o report...')
  canal = bot.get_channel(754741603230416896)
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


@bot.command()
async def reportar(ctx, *, text=None):
  z = discord.Embed(title='Novo Erro!', description='Carregando o report...')
  dm = bot.get_user(heitor)
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


@bot.command(aliases=['team', 'lara', 'eq'])
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


@bot.command()
async def clear(ctx, n=0):
  if n <= 0:
    await ctx.send('Você precisa digitar a quantidade de menssagens para serem deletadas')
  else:
    await ctx.channel.purge(limit=int(n))
    x = discord.Embed(title='Sistema de Limpar!')
    x.add_field(name='Menssagens deletadas:', value=n)
    x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    x.timestamp = datetime.datetime.utcnow()
    msg = await ctx.send(embed=x)


@bot.command()
async def darth(ctx):
  x = discord.Embed(title="Darth Gemidos!")
  x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  x.timestamp = datetime.datetime.utcnow()
  msg = await ctx.send(embed=x)


@bot.command(alises=['foto', 'img'])
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


@bot.command()
async def botinfo(ctx):
  calc = bot.latency * 1000
  pong = round(calc)
  a = bot.get_user(heitor)
  b = bot.get_user(tess)
  c = bot.get_user(ikki)
  x = discord.Embed(title='Bot Info:')
  x.add_field(name='Nome:', value=bot.user.display_name, inline=True)
  x.add_field(name='ID:', value=bot.user.id, inline=True)
  x.add_field(title='Ping:', value=pong, inline=True)
  x.add_field(name='Criado em:', value=bot.user.created_at.strftime('Data: %d/%m/%Y Hora: %H:%M:%S %p'), inline=True)
  x.add_field(name='criador:', value=a.display_name, inline=False)
  x.add_field(name='Equipe:', value=f'{b.display_name} e {c.display_name}', inline=False)
  x.set_thumbnail(url=bot.avatar_url)
  x.timestamp = datetime.datetime.utcnow()
  msg = await ctx.send(embed=x)
  await msg.add_reaction('<:LaraBoT:773736694733996062>')


@bot.command(aliases=['ferreiro', 'aviao', 'ar', 'empresa'])
async def sukhoi(ctx):
    ooo = discord.Embed(title='Sukhoi', description='...')
    a = discord.Embed(title='Ferreiro', description='Heitor, pesquisa sukhoi no google.')
    b = discord.Embed(title='Heitor', description='Porr@ ferreiro, uma empresa!')
    c = discord.Embed(title='Ferreiro', description='Agora coloca em imagens.')
    d = discord.Embed(title='Heitor', description='PORR@ FERREIRO!')
    #######
    msg = await ctx.send(embed=a)
    await asyncio.sleep(2.0)
    await msg.edit(embed=ooo)
    await asyncio.sleep(2.0)
    await msg.edit(embed=b)
    await asyncio.sleep(2.0)
    await msg.edit(embed=c)
    await asyncio.sleep(2.0)
    await msg.edit(embed=ooo)
    await asyncio.sleep(2.0)
    await msg.edit(embed=d)


@bot.command(aliases=['ruim', 'mds'])
async def ruler(ctx):
    ooo = discord.Embed(title='Rpg do Ruler', description='...')
    a = discord.Embed(title='Ruler', description='Beleza, rola o d20.')
    b = discord.Embed(title='Mateus', description='Deu 20!')
    c = discord.Embed(title='Ruler', description='Cê acerta o monstro.')
    d = discord.Embed(title='Mateus', description='A blz')
    e = discord.Embed(title='Mateus', description='O raio sai das minhas mãos.')
    f = discord.Embed(title='Ruler', description='Não, não. O raio veio do céu.')
    g = discord.Embed(title='Mateus', description='Pera... Ele atravessou a caverna?')
    h = discord.Embed(title='Ruler', description='Não. Ele veio do céu, fez uma curva e entrou pela entrada da caverna e acertou o bicho.')
    i = discord.Embed(title='Erick', description='COMO ASSIM, O RAIO FEZ DRIFT?')
    j = discord.Embed(title='Ruler', description='Sim!')
    k = discord.Embed(title='Erick', description='A')
    #######
    msg = await ctx.send(embed=a)
    await asyncio.sleep(2.0)
    await msg.edit(embed=ooo)
    await asyncio.sleep(2.0)
    await msg.edit(embed=b)
    await asyncio.sleep(2.0)
    await msg.edit(embed=c)
    await asyncio.sleep(2.0)
    await msg.edit(embed=d)
    await asyncio.sleep(2.0)
    await msg.edit(embed=e)
    await asyncio.sleep(2.0)
    await msg.edit(embed=f)
    await asyncio.sleep(2.0)
    await msg.edit(embed=g)
    await asyncio.sleep(2.0)
    await msg.edit(embed=h)
    await asyncio.sleep(5.0)
    await msg.edit(embed=i)
    await asyncio.sleep(2.0)
    await msg.edit(embed=j)
    await asyncio.sleep(2.0)
    await msg.edit(embed=k)


@bot.command()
async def rolls(ctx, d=0, x=0):
  r = []
  while 0 < d:
    r.append(random.randint(1, x))
    d = (d - 1)
  await ctx.send(r)

bot.run(token)