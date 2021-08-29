import discord
from discord.ext import commands
import random
import datetime
import asyncio

class economia_cog(commands.Cog):
    def __init__(self, lara):
        self.lara = lara

    @commands.command(aliases=['shop'])
    async def loja(self, ctx):
        y = discord.Embed(title='**Loja!**', description='Abrindo a loja...')
      #
        x = discord.Embed(title='**Loja!**', description='itens da loja Lara: use: !comprar (nome do item) para comprar!')
        x.add_field(name='📱**Celular:**', value='`1000$`', inline=True)
        x.add_field(name='💻 **PC:**', value='`5000$`', inline=True)
        x.add_field(name='⛏ **Picareta:**', value='`20$`', inline=True)
        x.add_field(name='⛏ **10x Picaretas:**', value='~~`200$`~~ => `180$`', inline=True)
        x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        x.timestamp = datetime.datetime.utcnow()
        msg = await ctx.send(embed=y)
        await asyncio.sleep(0.3)
        await msg.edit(embed=x)
        await msg.add_reaction('💵')

def setup(lara):
    lara.add_cog(economia_cog(lara))