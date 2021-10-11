import json
import discord
from discord.ext import commands
import random
import datetime
import asyncio

with open('config.json') as e:
    infos = json.load(e)
    heitor = infos['heitor']
    tess = infos['tess']
    ikki = infos['ikki']
    emanuel = infos['emanuel']

class outros_cog(commands.Cog):
	def __init__(self, lara):
		self.lara = lara

	@commands.command(aliases=['developer'])
	async def dev(self, ctx):
		if ctx.author.id == heitor:
			await ctx.send('Você é o desenvolvedor!')
		else:
			await ctx.send('Você não é o desenvolvedor!')


	@commands.command(aliases=['tess'])
	async def T(self, ctx):
		x = discord.Embed(title='**TESS-CHAN**', description=f'Você é uma pessoa incrível, realmente sou muito sortudo por ter você como amiga!')
		x.timestamp = datetime.datetime.utcnow()
		if ctx.author.id == tess:
			msg = await ctx.channel.send(embed=x)
			await msg.add_reaction('❤')
			await msg.add_reaction('😃')
		else:
			msg = await ctx.send('Você não é a Tess!')
			await msg.add_reaction('😒')


	@commands.command(aliases=['team', 'lara', 'eq'])
	async def equipe(self, ctx):
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
		elif ctx.author.id == emanuel:
			x = discord.Embed(title='Olá 100tavos!', description='*Bora dar um `!ban @everyone`?')
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

	@commands.command()
	async def ik(self, ctx):
		a = await ctx.send('Tu é?')
		await asyncio.sleep(2.0)
		await ctx.send('Ihh Rapaiz')

	@commands.command()
	async def defala(self, ctx):
		if ctx.author.id == 646167529043263509:
			await ctx.send('')
		else:
			await ctx.send('Você não é Defala!')

	@commands.command(aliases=['game', 'cube'])
	async def hairo(self, ctx):
		x = discord.Embed(title=f'Geometry Hunter', url='https://hairohukosu.excepti0n.repl.co/')
		x.add_field(name=f'Criação:', value=f'Criado por HairoHukosu, **Geometry Hunter** é um jogo que inicialmente foi criado em apenas uma semana, mas ainda recebe atualizações.', inline=False)
		x.add_field(name=f'Sobre:', value=f'O jogo se trata em que o protagonista que é um cubo azul deve derrotar um mostro de apenas um olho.', inline=False)
		x.set_thumbnail(url='https://cdn.discordapp.com/attachments/753004109790969867/893159772336054282/1633016277829.png')
		x.timestamp = datetime.datetime.utcnow()
		msg = await ctx.send(embed=x)
		await msg.add_reaction('<:cube:893157937890074714>')


	@commands.command()
	async def bn(self, ctx, membro: discord.Member):

		message = await ctx.send(f"Are you sure you want to ban {membro}?")
		check = lambda m: m.author == ctx.author and m.channel == ctx.channel

		try:
			confirm = await self.lara.wait_for("message", check=check, timeout=30)
		except asyncio.TimeoutError:
			await message.edit(content="Ban cancelled, timed out.")
			return

		if confirm.content == "yes":
			await message.edit(content=f"{member} has been banned.")
			return

		await message.edit(content="Ban cancelled.")

def setup(lara):
	lara.add_cog(outros_cog(lara))