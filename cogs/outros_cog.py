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

	@commands.command(aliases=['clean', 'limpar'])
	async def clear(self, ctx, n=0):
		if n <= 0:
			await ctx.send('Você precisa digitar a quantidade de menssagens para serem deletadas')
		else:
			await ctx.channel.purge(limit=int(n))
			x = discord.Embed(title='Sistema de Limpar!')
			x.add_field(name='Menssagens deletadas:', value=f'{n}')
			x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			x.timestamp = datetime.datetime.utcnow()
			msg = await ctx.send(embed=x)


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

def setup(lara):
	lara.add_cog(outros_cog(lara))