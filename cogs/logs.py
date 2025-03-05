import discord, os, datetime
from discord.ext import commands, tasks

class logs_cog(commands.Cog):
	def __init__ (self, lara):
		self.lara = lara

	@commands.Cog.listener()
	async def on_command(self, ctx):
		server = ctx.guild.name
		user = ctx.author.id
		comando = ctx.command
		timestamp = datetime.datetime.utcnow().strftime(f'Data: %d/%m/%Y Hora: %H:%M:%S %p')

		with open('logs.txt', 'a') as ls:
			ls.write(f'{server} > {user} > {comando} > {timestamp}\n')
		ls.close()

def setup(lara):
	lara.add_cog(logs_cog(lara))
