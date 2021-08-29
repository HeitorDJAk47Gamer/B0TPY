import discord
from discord.ext import commands
import random
import datetime
import asyncio

class utilidade_cog(commands.Cog):
	def __init__(self, lara):
		self.lara = lara

	@commands.command()
	async def membros(self, ctx):
		mb = len(ctx.guild.members)
		await ctx.send(f'Este servidor possui: {mb} membros')

	@commands.command(alises=['foto', 'img'])
	async def avatar(self, ctx, membro : discord.Member = 'nada'):
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

	@commands.command()
	async def user(self, ctx, membro : discord.Member = 'nada'):
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


	@commands.command(aliases=['sv', 'servidor'])
	async def server(self, ctx):
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


	@commands.command(aliases=['repetir'])
	async def say(self, ctx, *, message):
		if message != '':
			await ctx.send(message)
		else:
			await ctx.send('Por favor, dê alguma mensagem!')


	@commands.command()
	async def code(self, ctx, prog=None, *, code):
		user = ctx.message.author.display_name
		if message != '':
			await ctx.send(f'**código de:** `{user}` ```{prog}\n{code}\n```')
			await ctx.message.delete()
		else:
			await ctx.send('Por favor, insira o código!')

def setup(lara):
	lara.add_cog(utilidade_cog(lara))