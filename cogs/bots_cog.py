import discord
from discord.ext import commands
import random
import datetime
import asyncio


class bots_cog(commands.Cog):
	def __init__(self, lara):
		self.lara = lara

	@commands.command(aliases=['info'])
	async def bot(self, ctx):
		calc = self.lara.latency * 1000
		pong = round(calc)
		x = discord.Embed(title='<a:pinkarrow:882604328400093194> Bot Info:', color=0xffcbdb)
		x.add_field(name='📝 Nome:', value=self.lara.user.display_name, inline=True)
		x.add_field(name='🆔 ID:', value=self.lara.user.id, inline=True)
		x.add_field(name='🇧🇷 Região:', value='Brasil', inline=True)
		x.add_field(name='👥 Membros Globais:', value=f'{len(self.lara.users)}', inline=True)
		x.add_field(name='🌎 Servidores Globais:', value=f'{len(self.lara.guilds)}', inline=True)
		x.add_field(name='<:space_bottle:882600683205967912> Ping:', value=f'{pong} `ms`', inline=True)
		x.add_field(name='📅 Criado em:', value=self.lara.user.created_at.strftime(f'Data: %d/%m/%Y \n Hora: %H:%M:%S %p'), inline=True)
		x.set_thumbnail(url=self.lara.user.avatar_url)
		x.timestamp = datetime.datetime.utcnow()
		await ctx.send(embed=x)
		

	@commands.command()
	async def ping(self, ctx):
		calc = self.lara.latency * 1000
		pong = round(calc)

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
	
