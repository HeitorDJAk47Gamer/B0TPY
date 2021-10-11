import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, has_permissions, MissingPermissions
import random
import datetime
import asyncio

class utilidade_cog(commands.Cog):
	def __init__(self, lara):
		self.lara = lara

	@commands.command()
	async def membros(self, ctx):
		total = len(ctx.guild.members)
		online = len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members)))
		idle = len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members)))
		dnd = len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members)))
		offline = len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))
		us = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
		bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
		x = discord.Embed(title=f'👥 Membros: {total}')
		x.add_field(name=f'🟢 Online:', value=f'{online}', inline=True)
		x.add_field(name=f'🌙 Ausente:', value=f'{idle}', inline=True)
		x.add_field(name=f'⛔ Não Perturbe:', value=f'{dnd}', inline=True)
		x.add_field(name=f'🌑 Offline:', value=f'{offline}', inline=True)
		x.add_field(name=f'🤖 Bot:', value=f'{bots}', inline=True)
		x.add_field(name=f'👤 Usuários:', value=f'{us}', inline=True)
		x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
		x.timestamp = datetime.datetime.utcnow()
		await ctx.send(embed=x)

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
			rm = []
			for role in membro.roles:
				if role.name != "@everyone":
					rm.append(role.mention)
			rms = "".join(rm)
			y = discord.Embed(title='', description=f'**Carregando**\n<a:typing:892412508332253224>')
			x = discord.Embed(title='**Informações:**')
			x.add_field(name='Nome:', value=membro.display_name, inline=True)
			x.add_field(name='ID:', value=membro.id, inline=True)
			x.add_field(name='Status:', value=f'`{membro.status}`', inline=True)
			x.add_field(name='Criado em:', value=membro.created_at.strftime(f'Data: %d/%m/%Y \n Hora: %H:%M:%S %p'), inline=True)
			x.add_field(name='Entrou em:', value=membro.joined_at.strftime(f'Data: %d/%m/%Y \n Hora: %H:%M:%S %p'), inline=True)
			x.add_field(name=f'Cargos:', value=f'{rms}', inline=False)
			x.set_thumbnail(url=membro.avatar_url)
			x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			x.timestamp = datetime.datetime.utcnow()
			msg = await ctx.send(embed=y)
			await asyncio.sleep(0.5)
			await msg.edit(embed=x)
		else:
			rm = []
			for role in ctx.author.roles:
				if role.name != "@everyone":
					rm.append(role.mention)
			rms = "".join(rm)
			y = discord.Embed(title='', description=f'**Carregando**\n<a:typing:892412508332253224>')
			x = discord.Embed(title='**Informações:**')
			x.add_field(name='Nome:', value=ctx.author.display_name, inline=True)
			x.add_field(name='ID:', value=ctx.author.id, inline=True)
			x.add_field(name='Status:', value=f'`{ctx.author.status}`', inline=True)
			x.add_field(name='Criado em:', value=ctx.author.created_at.strftime(f'Data: %d/%m/%Y \n Hora: %H:%M:%S %p'), inline=True)
			x.add_field(name='Entrou em:', value=ctx.author.joined_at.strftime(f'Data: %d/%m/%Y \n Hora: %H:%M:%S %p'), inline=True)
			x.add_field(name=f'Cargos:', value=f'{rms}', inline=False)
			x.set_thumbnail(url=ctx.author.avatar_url)
			x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			x.timestamp = datetime.datetime.utcnow()
			msg = await ctx.send(embed=y)
			await asyncio.sleep(0.5)
			await msg.edit(embed=x)


	@commands.command(aliases=['sv', 'servidor'])
	async def server(self, ctx):
		rm = []
		for role in ctx.guild.roles:
			if role.name != "@everyone":
				rm.append(role.mention)
		rms = "".join(rm)
		membros = len(ctx.guild.members)
		cargos = len(ctx.guild.roles)
		texto = len(ctx.guild.text_channels)
		voz = len(ctx.guild.voice_channels)
		canal = int(texto + voz)
		cat = len(ctx.guild.categories)
		lvl = ctx.guild.verification_level
		boost = int(ctx.guild.premium_subscription_count)
		x = discord.Embed(title='**Informações:**')
		x.add_field(name=f'📝 Nome:', value=f'{ctx.guild.name}', inline=False)
		x.add_field(name=f'🆔 ID:', value=f'`{ctx.guild.id}`', inline=True)
		x.add_field(name=f'👑 Dono:', value=ctx.guild.owner.mention, inline=True)
		x.add_field(name=f'📅 Criado em:', value=ctx.guild.created_at.strftime(f'Data: %d/%m/%Y \n Hora: %H:%M:%S %p'), inline=True)
		x.add_field(name=f'🌎 Região:', value=f'`{ctx.guild.region}`', inline=True)
		x.add_field(name=f'👥 Membros:', value=f'`{membros}`', inline=True)
		x.add_field(name=f'📡 Canais:', value=f'`{canal}`', inline=True)
		x.add_field(name=f'🔰 Verificação:', value=f'`{lvl}`', inline=True)
		x.add_field(name=f'<:boost:881920170136854558> Boost:', value=f'{boost}', inline=True)
		x.add_field(name=f'📂 Categorias:', value=f'`{cat}`', inline=False)
		x.add_field(name=f'💬 Texto:', value=f'`{texto}`', inline=True)
		x.add_field(name=f'🔊 Voz:', value=f'`{voz}`', inline=True)
		x.add_field(name=f'🔐 Cargos: `({cargos})`', value=f'{rms}', inline=False)
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
		user = ctx.author.display_name
		if code != '':
			await ctx.send(f'**código de:** `{user}` ```{prog}\n{code}\n```')
			await ctx.message.delete()
		else:
			await ctx.send('Por favor, insira o código!')

	@commands.command()
	async def emojis(self, ctx):
		x = []
		w = []
		for emoji in ctx.guild.emojis:
			if emoji.animated:
				if not emoji.managed:
					z = f'<a:{emoji.name}:{emoji.id}>'
					w.append(z)
			else:
				if not emoji.managed:
					y = f'<:{emoji.name}:{emoji.id}>'
					x.append(y)
		emojix = "".join(x)
		emojiw = "".join(w)
		await ctx.send(f'Emojis Não animados: {emojix}\nEmojis Animados: {emojiw}')

	@commands.command(aliases=['clean', 'limpar'])
	@has_permissions(manage_messages=True)
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

	@commands.command()
	async def emlist(self, ctx):
		if ctx.channel.id == 893942602443915314:
			await ctx.channel.purge(limit=int(10))
		x = []
		w = []
		for emoji in ctx.guild.emojis:
			if emoji.animated:
				if not emoji.managed:
					z = f'<a:{emoji.name}:{emoji.id}> `<a:{emoji.name}:{emoji.id}>`\n'
					w.append(z)
			else:
				if not emoji.managed:
					y = f'<:{emoji.name}:{emoji.id}> `<:{emoji.name}:{emoji.id}>`\n'
					x.append(y)
		emojix = "".join(x)
		emojiw = "".join(w)
		await ctx.send(f'Emojis não Animados:\n{emojix}')
		await ctx.send(f'Emojis Animados:\n{emojiw}')

	@commands.command()
	async def timer(self, ctx, tempo=0, *,texto='Pronto!'):
		x = discord.Embed(title=f'Temporizador ativado!', description=f'Temporizador marcado em {tempo} segundos.')
		y = discord.Embed(title=f'Temporizador desativado!', description=f'{texto}\n{ctx.author.mention}')
		msg = await ctx.send(embed=x)
		await asyncio.sleep(tempo)
		await msg.edit(embed=y)

	@commands.command()
	async def roles(self, ctx):
		rm = []
		for role in ctx.guild.roles:
			if role.name != "@everyone":
				rm.append(role.mention)
		rms = "".join(rm)
		x = discord.Embed(tile=f'Cargos de {ctx.guild.name}', description=f'{rms}')
		x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
		x.timestamp = datetime.datetime.utcnow()
		await ctx.send(embed=x)

def setup(lara):
	lara.add_cog(utilidade_cog(lara))