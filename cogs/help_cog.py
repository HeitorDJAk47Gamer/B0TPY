import json
import discord
from discord.ext import commands
import random
import datetime
import asyncio
prefixes = '-'

with open('config.json') as e:
	infos = json.load(e)
	heitor = infos['heitor']
	tess = infos['tess']
	ikki = infos['ikki']
	emanuel = infos['emanuel']

class help_cog(commands.Cog):
	def __init__(self, lara):
		self.lara = lara

	@commands.group(invoke_without_command=True, aliases=['ajuda', 'helper'])
	async def help(self, ctx):
		x = discord.Embed(title='Lista de comandos:', description=f'Use {prefixes}help (comando) para obter mais informações!')
		x.add_field(name='Bot', value='Bot, Feed, Report, Sug, Ping', inline=False)
		x.add_field(name='Diversão', value='Dado, hug, Anime, D&D, Moeda', inline=False)
		x.add_field(name='Utilidades', value='Server, User, Membros, Say, Code, Avatar', inline=False)
		x.add_field(name='Moderação', value='Ban, Kick, Cargo', inline=False)
		x.add_field(name='Economia', value='Loja', inline=False)
		await ctx.send(embed=x)

	@help.command(aliases=['expulsar'])
	async def kick(self, ctx):
		x = discord.Embed(title='Expulsar')
		x.add_field(name='Categoria:', value='Moderação', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[kick, expulsar]', inline=True)
		x.add_field(name='Descrição:', value='Comando para expulsar um membro do servidor.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866689638390038608/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['banir'])
	async def ban(self, ctx):
		x = discord.Embed(title='Banir')
		x.add_field(name='Categoria:', value='Moderação', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[ban, banir]', inline=True)
		x.add_field(name='Descrição:', value='Comando para banir um membro do servidor.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866689959662845982/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['add', 'role'])
	async def cargo(self, ctx):
		x = discord.Embed(title='Cargo')
		x.add_field(name='Categoria:', value='Moderação', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[cargo, add, role]', inline=True)
		x.add_field(name='Descrição:', value='Comando para adicionar um cargo a um determinado membro.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866690432145555456/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['animes'])
	async def anime(self, ctx):
		x = discord.Embed(title='Anime')
		x.add_field(name='Categoria:', value='Diversão', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[anime, animes]', inline=True)
		x.add_field(name='Descrição:', value='Uma imagem de anime aleatória.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866691020859506738/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['roll'])
	async def dado(self, ctx):
		x = discord.Embed(title='Dado')
		x.add_field(name='Categoria:', value='Diversão', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[dado, roll]', inline=True)
		x.add_field(name='Descrição:', value='Para rolar um dado ou mais dados com modificardores (- ou +), de qualquer valor.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866692098010513428/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['cara', 'coroa'])
	async def moeda(self, ctx):
		x = discord.Embed(title='Moeda')
		x.add_field(name='Categoria:', value='Diversão', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[moeda, cara, coroa]', inline=True)
		x.add_field(name='Descrição:', value='Comando de cara ou coroa.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866692474347847720/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['d&d'])
	async def dnd(self, ctx):
		x = discord.Embed(title='D&D')
		x.add_field(name='Categoria:', value='Diversão', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[dnd, d&d]', inline=True)
		x.add_field(name='Descrição:', value='Comando para ajudar jogadores de Dungeons & Dragons.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866693189137203270/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['abraçar'])
	async def hug(self, ctx):
		x = discord.Embed(title='Abraço')
		x.add_field(name='Categoria:', value='Diversão', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[abraçar, hug]', inline=True)
		x.add_field(name='Descrição:', value='Dê um abraço em alguém.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866693413734449182/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['info'])
	async def bot(self, ctx):
		x = discord.Embed(title='Bot')
		x.add_field(name='Categoria:', value='Bot', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[bot, info]', inline=True)
		x.add_field(name='Descrição:', value='Comando para exibir informações do bot.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866694232924225576/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['reportar'])
	async def report(self, ctx):
		x = discord.Embed(title='Reportar')
		x.add_field(name='Categoria:', value='Bot', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[report, reportar]', inline=True)
		x.add_field(name='Descrição:', value='Para reportar erros ou bugs do bot para a equipe.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866696841491644473/unknown.png')
		await ctx.send(embed=x)

	@help.command()
	async def ping(self, ctx):
		x = discord.Embed(title='Ping')
		x.add_field(name='Categoria:', value='Bot', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[ping]', inline=True)
		x.add_field(name='Descrição:', value='Mostrar latência atual do bot.', inline=False)
		x.set_image(url='https://media.discordapp.net/attachments/866686570894196746/866695015211335680/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['feedback', 'back'])
	async def feed(self, ctx):
		x = discord.Embed(title='FeedBack')
		x.add_field(name='Categoria:', value='Bot', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[feed, feedback, back]', inline=True)
		x.add_field(name='Descrição:', value='Envie seu FeedBack para a equipe.', inline=False)
		await ctx.send(embed=x)

	@help.command(aliases=['sugerir', 'sugestao'])
	async def sug(self, ctx):
		x = discord.Embed(title='Sugestao')
		x.add_field(name='Categoria:', value='Bot', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[sug, sugestao, sugerir]', inline=True)
		x.add_field(name='Descrição:', value='Envie sua sugestão para a equipe.', inline=False)
		await ctx.send(embed=x)

	@help.command(aliases=['sv', 'servidor'])
	async def server(self, ctx):
		x = discord.Embed(title='Server')
		x.add_field(name='Categoria:', value='Utilidades', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[server, servidor, sv]', inline=True)
		x.add_field(name='Descrição:', value='Comando para exibir informações do servidor.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866694485009891405/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['foto', 'img'])
	async def avatar(self, ctx):
		x = discord.Embed(title='Avatar')
		x.add_field(name='Categoria:', value='Utilidades', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[avatar, img, foto]', inline=True)
		x.add_field(name='Descrição:', value='Mostrar avatar.', inline=False)
		await ctx.send(embed=x)

	@help.command()
	async def user(self, ctx):
		x = discord.Embed(title='User')
		x.add_field(name='Categoria:', value='Utilidades', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[user]', inline=True)
		x.add_field(name='Descrição:', value='Comando para exibir informações do usuário citado.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866694392432427008/unknown.png')
		await ctx.send(embed=x)

	@help.command()
	async def membros(self, ctx):
		x = discord.Embed(title='Membros')
		x.add_field(name='Categoria:', value='Utilidades', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[membros]', inline=True)
		x.add_field(name='Descrição:', value='Membros totais no servidor.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866694879216402472/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['repetir'])
	async def say(self, ctx):
		x = discord.Embed(title='Say')
		x.add_field(name='Categoria:', value='Utilidades', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[say, repetir]', inline=True)
		x.add_field(name='Descrição:', value='Repetir o que foi digitado no comando.', inline=False)
		x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/866695658646667275/unknown.png')
		await ctx.send(embed=x)

	@help.command()
	async def code(self, ctx):
		x = discord.Embed(title='Code')
		x.add_field(name='Categoria:', value='Utilidades', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[code]', inline=True)
		x.add_field(name='Descrição:', value='Formate seu código instantaneamente.', inline=False)
		x.set_image(url='https://media.discordapp.net/attachments/866686570894196746/866696352225820702/unknown.png')
		await ctx.send(embed=x)

	@help.command(aliases=['limpar', 'clean'])
	async def clear(self, ctx):
		x = discord.Embed(title='Clear')
		x.add_field(name='Categoria:', value='Utilidades', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[clear, limpar, clean]', inline=True)
		x.add_field(name='Descrição:', value='Caso precise limpar algum chat.', inline=False)
		await ctx.send(embed=x)

	@help.command(aliases=['shop'])
	async def loja(self, ctx):
		x = discord.Embed(title='Loja')
		x.add_field(name='Categoria:', value='Economia', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[loja, shop]', inline=True)
		x.add_field(name='Descrição:', value='Veja os itens disponíveis para comprar na Loja Lara!', inline=False)
		await ctx.send(embed=x)

	@help.command(aliases=['música', 'musica'])
	async def music(self, ctx):
		x = discord.Embed(title='Sistema de música', url='https://discord.com/oauth2/authorize?client_id=754474576078962769&scope=bot&permissions=8', description='Clique em Sistema de música para convidar Flitser.')
		x.add_field(name='Categoria:', value='Música', inline=True)
		x.add_field(name='Sintaxe:', value=f'{prefixes}[music, musica]', inline=True)
		x.add_field(name='Descrição:', value='No momento não temos comandos de música disponíveis´, porém temos nosso bot de música!', inline=False)
		x.set_image(url='https://media.discordapp.net/attachments/771439991846862948/881948701390667836/1630343344530.png?width=409&height=409')
		await ctx.send(embed=x)

def setup(lara):
	lara.add_cog(help_cog(lara))