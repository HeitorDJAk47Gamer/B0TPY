import discord
from discord.ext import commands
import random
import datetime
import asyncio

class diversao_cog(commands.Cog):
    def __init__(self, lara):
        self.lara = lara

    @commands.command(aliases=['abraçar'])
    async def hug(self, ctx, membro : discord.Member):
        x = discord.Embed(title='Abraçooo!', description=f'{ctx.author.mention} abraçou {membro.mention}')
        x.set_image(url='https://media1.tenor.com/images/ea1ca14e49866429e2221aab2126cdb0/tenor.gif?itemid=14599424')
        x.timestamp = datetime.datetime.utcnow()
        msg = await ctx.send(embed=x)
        await msg.add_reaction('❤')


    @commands.command(aliases=['roll'])
    async def dado(self, ctx, dice, h='nada', mod=0):
        diceFindD = dice.find('d')
        dice1 = dice[:diceFindD].replace('d', '')
        dice2 = dice[diceFindD:].replace('d', '')
        r = []
        if dice1 == '':
            dice1 = 1
        for y in range(int(dice1)):
            r.append(random.randint(1, int(dice2)))
        total = sum(r)
        y = discord.Embed(title='Dados', description='🎲 Rolando dado...')
        if h == 'nada':
            x = discord.Embed(title=f'**{dice1}D{dice2}**', description=f'{r} = {total}')
            x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            x.timestamp = datetime.datetime.utcnow()
            msg = await ctx.send(embed=y)
            await asyncio.sleep(0.7)
            await msg.edit(embed=x)
            await msg.add_reaction('🎲')
        elif h == '-':
            sub = (total - mod)
            x = discord.Embed(title=f'**{dice1}D{dice2}**', description=f'{r} - {mod} = {sub}')
            x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            x.timestamp = datetime.datetime.utcnow()
            msg = await ctx.send(embed=y)
            await asyncio.sleep(0.7)
            await msg.edit(embed=x)
            await msg.add_reaction('🎲')
        elif h == '+':
            soma = (total + mod)
            x = discord.Embed(title=f'**{dice1}D{dice2}**', description=f'{r} + {mod}  = {soma}')
            x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            x.timestamp = datetime.datetime.utcnow()
            msg = await ctx.send(embed=y)
            await asyncio.sleep(0.7)
            await msg.edit(embed=x)
            await msg.add_reaction('🎲')
        elif h == '*':
            mul = (total * mod)
            x = discord.Embed(title=f'**{dice1}D{dice2}**', description=f'{r} * {mod}  = {mul}')
            x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            x.timestamp = datetime.datetime.utcnow()
            msg = await ctx.send(embed=y)
            await asyncio.sleep(0.7)
            await msg.edit(embed=x)
            await msg.add_reaction('🎲')
        elif h == '/':
            div = (total / mod)
            x = discord.Embed(title=f'**{dice1}D{dice2}**', description=f'{r} / {mod}  = {div}')
            x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            x.timestamp = datetime.datetime.utcnow()
            msg = await ctx.send(embed=y)
            await asyncio.sleep(0.7)
            await msg.edit(embed=x)
            await msg.add_reaction('🎲')
        else:
            await ctx.reply('**Você precisa definir um número máximo!**')


    @commands.command(aliases=['cara', 'coroa'], help='Jogue cara ou coroa!')
    async def moeda(self, ctx):
        var = random.randint(1, 2)
        if var == 1:  # cara
            msg = await ctx.send('Deu cara!')
            await msg.add_reaction('😀')
        elif var == 2:  # coroa
            msg = await ctx.send('Deu coroa!')
            await msg.add_reaction('👑')

    @commands.command()
    async def ejetar(self, ctx, membro: discord.Member):
        texto = ['é o impostor', 'é o tripulante']
        rev = random.choice(texto)
        amugus = discord.Embed(title=f'{membro.name} foi ejetado')
        amugus.timestamp=datetime.datetime.utcnow()
        amugus.set_image(url='https://cdn.discordapp.com/attachments/753004109790969867/895392496866164798/arpEpajbLXbqN4KpSqpVw5obsEMfZiGE0ro0YhkdK1QFThdC3fAZkOapCeeP3lQAAAABJRU5ErkJggg.png')
        revelado = discord.Embed(title=f'{membro.name} {rev}')
        revelado.timestamp=datetime.datetime.utcnow()

        msg = await ctx.send(embed=amugus)
        await asyncio.sleep(5)
        await msg.edit(embed=revelado)

def setup(lara):
    lara.add_cog(diversao_cog(lara))
