import random
import discord
import asyncio
import datetime
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType, has_permissions, MissingPermissions

class Erros(commands.Cog):

	def __init__(self, lara):
		self.lara = lara

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandNotFound):
			msg = discord.Embed(title=f'Comando não encontrado', description=f'Desculpe-me mas, o comando não foi encontrado!\nVerifique se digitou o comando corretamente.', color=0xff0000)

		elif isinstance(error, MissingPermissions):
			msg = discord.Embed(title=f'Permissão não atribuída!', description=f'Você não possue permissão para executar essa função!', color=0xff0000)
			
		elif isinstance(error, commands.CommandOnCooldown):
			msg = discord.Embed(title=f'Calma ae bro!',description=f'tente denovo em: {int(error.retry_after)}s.', color=0xff0000)

		elif isinstance(error, commands.UserInputError):
			msg = discord.Embed(title=f'Erro de entrada!', description=f'Por favor, coloque a informação pedida!', color=0xff0000)

		else:
			msg = discord.Embed(title=f'Erro!', description=f'Comando não pode ser executado!', color=0xff0000)

		msg.set_footer(text=f'{self.lara.user}', icon_url=self.lara.user.avatar_url)

		await ctx.send(embed=msg, delete_after=5)
		await ctx.message.delete(delay=5)


def setup(lara):
	lara.add_cog(Erros(lara))
