import json
import discord
from discord.ext import commands
import random
import datetime
import asyncio

with open('config.json') as e:
	infos = json.load(e)
	prefixo = infos['prefix']
	heitor = infos['heitor']
	tess = infos['tess']
	ikki = infos['ikki']
	emanuel = infos['emanuel']
	chsug = infos['chsug']
	chfeed = infos['chfeed']
	chrpt = infos['chrpt']

lara = commands.Bot(command_prefix=prefixo)

class bots_cog(commands.Cog):
	def __init__(self, lara):
		self.lara = lara

	@commands.command(aliases=['info'])
	async def bot(self, ctx):
		calc = self.lara.latency * 1000
		pong = round(calc)
		x = discord.Embed(title='Bot Info:')
		x.add_field(name='Nome:', value=self.lara.user.display_name, inline=True)
		x.add_field(name='ID:', value=self.lara.user.id, inline=True)
		x.add_field(name='Ping:', value=f'{pong} `ms`', inline=True)
		x.add_field(name='Criado em:', value=self.lara.user.created_at.strftime('Data: %d/%m/%Y Hora: %H:%M:%S %p'), inline=False)
		x.add_field(name='criador:', value=self.lara.get_user(heitor).display_name, inline=True)
		x.add_field(name='Equipe:', value=f'{self.lara.get_user(tess).display_name} e {self.lara.get_user(ikki).display_name}', inline=True)
		x.set_thumbnail(url=self.lara.user.avatar_url)
		x.timestamp = datetime.datetime.utcnow()
		msg = await ctx.send(embed=x)
		await msg.add_reaction('<:LaraBoT:773736694733996062>')


	@commands.command(aliases=['feedback', 'back'])
	async def feed(self, ctx, *, message):
		canal = self.lara.get_channel(chfeed)
		x = discord.Embed(title='Nova FeedBack')
		x.add_field(name='Membro:', value=ctx.author, inline=False)
		x.add_field(name='`FeedBack:`', value=message, inline=False)
		x.timestamp = datetime.datetime.utcnow()
		await canal.send(embed=x)
		await ctx.message.add_reaction('✅')


	@commands.command(aliases=['contribuir', 'sugestao', 'sugerir'])
	async def sug(self, ctx, *, message):
		canal = self.lara.get_channel(chsug)
		x = discord.Embed(title='Nova sugestão')
		x.add_field(name='Membro:', value=ctx.author, inline=False)
		x.add_field(name='`Sugerido:`', value=message, inline=False)
		x.timestamp = datetime.datetime.utcnow()
		await canal.send(embed=x)
		await ctx.message.add_reaction('✅')


	@commands.command(aliases=['reportar'])
	async def report(self, ctx, *, texto=None):
		z = discord.Embed(title='Novo Erro!', description='Carregando o report...')
		canal = self.lara.get_channel(chrpt)
		x = discord.Embed(title='**Report de Erro!**')
		x.add_field(name='Server:', value=ctx.guild.name, inline=False)
		x.add_field(name='ID do Server:', value=ctx.guild.id, inline=False)
		x.add_field(name='Relatório:', value=texto, inline=False)
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


	@commands.command()
	async def ping(self, ctx):
		calc = self.lara.latency * 1000
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

def setup(lara):
	lara.add_cog(bots_cog(lara))
	