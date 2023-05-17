import discord, random, datetime, asyncio
from discord.ext import commands

class bots_cog(commands.Cog):
	def __init__(self, lara):
		self.lara = lara



	@commands.command(aliases=['feedback', 'back'])
	async def feed(self, ctx, *, message):
		canal = self.lara.get_channel(chfeed)
		x = discord.Embed(title='Nova FeedBack')
		x.add_field(name='Membro:', value=ctx.author, inline=False)
		x.add_field(name='`FeedBack:`', value=message, inline=False)
		x.timestamp = datetime.datetime.utcnow()
		await canal.send(embed=x)
		await ctx.message.add_reaction('<a:yeah:882026711376609360>')
#comando para feedback

	@commands.command(aliases=['contribuir', 'sugestao', 'sugerir'])
	async def sug(self, ctx, *, message):
		canal = self.lara.get_channel(chsug)
		x = discord.Embed(title='Nova sugestão')
		x.add_field(name='Membro:', value=ctx.author, inline=False)
		x.add_field(name='`Sugerido:`', value=message, inline=False)
		x.timestamp = datetime.datetime.utcnow()
		await canal.send(embed=x)
		await ctx.message.add_reaction('<a:yeah:882026711376609360>')
#comando de sugestão

	@commands.command(aliases=['reportar'])
	async def report(self, ctx, *, texto=None):
		s = self.lara.get_guild(servidor)
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
		await ctx.message.add_reaction('<a:yeah:882026711376609360>')
		#reação
		y = discord.Embed(title='#Equipe Lara B0T')
		y.add_field(name=f'**Olá {ctx.author.display_name}**', value='*Agradecemos pela sua colaboração com nosso projeto, iremos analisar o problema e solucioná-lo!*')
		y.set_thumbnail(url=s.icon_url)
		y.timestamp = datetime.datetime.utcnow()
		await ctx.author.send(embed=y)
#report


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
	
