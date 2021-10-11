import json
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, has_permissions, MissingPermissions
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
"""
    async def open_account(user):
        users = await get_bank_data()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)]['wallet'] = 0
            users[str(user.id)]['bank'] = 0
        with open('main_bank.json', 'w') as f:
            json.dump(users,f)
            return True

    async def get_bank_data():
        with open('main_bank.json', 'r') as f:
            users = json.load(f)
        return users

    @commands.command()
    async def balance(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        amt_wallet = users[str(user.id)]['wallet']
        amt_bank = users[str(user.id)]['bank']

        x = discord.Embed(title=f'{ctx.author.name} balanço')
        x.add_field(f'Carteira', value=f'${amt_wallet}', inline=True)
        x.add_field(f'Banco', value=f'${amt_bank}', inline=True)
        await ctx.send(embed=x)

    @commands.command(aliases=['dia', 'diaria'])
    @commands.cooldown(1, 60 * 60 * 24, commands.BucketType.user)
    async def daily(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()
        ads = random.randint(1, 100)
        await ctx.send(f'Sua diária é: ${ads}!')

        users[str(user.id)]['wallet'] += ads
        with open('main_bank.json', 'w') as f:
            json.dump(user,f)
"""
def setup(lara):
    lara.add_cog(economia_cog(lara))
