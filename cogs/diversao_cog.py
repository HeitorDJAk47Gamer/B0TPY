import json
import discord
from discord.ext import commands
import random
import datetime
import asyncio

with open('config.json') as e:
    infos = json.load(e)
    prefixo = infos['prefix']

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


    @commands.command(aliases=['animes'])
    async def anime(self, ctx):
        img = random.randint(1, 200)
        await ctx.send(f'https://larab0tbeta.heitordjak47.repl.co/galeria/{img}.jpg')


    @commands.group(invoke_without_command=True, aliases=['d&d'])
    async def dnd(self, ctx):
        z = '```'
        x = discord.Embed(title='**Comandos de D&D:**')
        x.add_field(name='*Compra de Ponto:*', value=f'{z}\n{prefixo}D&D cp\n{z}', inline=True)
        x.add_field(name='*Modificadores:*', value=f'{z}\n{prefixo}D&D mod\n{z}', inline=True)
        x.add_field(name='*Pré-definição de pontos:*', value=f'{z}\n{prefixo}D&D dp\n{z}', inline=True)
        x.add_field(name='*CD:*', value=f'{z}\n{prefixo}D&D cd\n{z}', inline=True)
        x.add_field(name='*Ficha:*', value=f'{z}\n{prefixo}D&D ficha\n{z}', inline=True)
        x.add_field(name='*Ouro:*', value=f'{z}\n{prefixo}D&D ouro\n{z}', inline=True)
        x.add_field(name='*Pacotes:*', value=f'{z}\n{prefixo}D&D pct\n{z}', inline=True)
        x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        x.timestamp = datetime.datetime.utcnow()
        msg = await ctx.send(embed=x)

    @dnd.command(aliases=['compra'])
    async def cp(self, ctx):
        x = discord.Embed(title='**Compra de Pontos**')
        x.set_image(url='https://cdn.discordapp.com/attachments/753004109790969867/853721835899715604/cp.png')
        await ctx.send(embed=x)

    @dnd.command(aliases=['modificardores', 'bonus'])
    async def mod(self, ctx):
        x = discord.Embed(title='**Modificadores**')
        x.set_image(url='https://cdn.discordapp.com/attachments/753004109790969867/853721845420261386/mod.png')
        await ctx.send(embed=x)

    @dnd.command(aliases=['distribuir'])
    async def dp(self, ctx):
        x = discord.Embed(title='**Distribuição de pontos pré-Definida**')
        x.add_field(name='*Você pode usar os seguintes valores:*', value='15, 14, 13, 12, 10, 8.', inline=False)
        x.add_field(name='*Diatribua esses valores entre:*', value='**Força, Destreza, Constituição, Inteligência, Sabedoria, Carisma**', inline=False)
        x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        x.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=x)

    @dnd.command(aliases=['classe', 'dificuldade'])
    async def cd(self, ctx):
        d = discord.Embed(title='**CD**')
        d.set_image(url='https://cdn.discordapp.com/attachments/753004109790969867/853721828162011146/cd.png')
        await ctx.send(embed=d)

    @dnd.command(aliases=['e5'])
    async def ficha(self, ctx):
        x = discord.Embed(title='**Ficha**', url='https://cdn.discordapp.com/attachments/753004109790969867/853721843785531422/dd-5e-ficha-de-personagem-automatica-biblioteca-elfica.pdf', description='Clique para baixar a ficha D&De5 em Português BR automática.')
        msg = await ctx.send(embed=x)
        await msg.add_reaction('<a:download:882601000945483776>')

    @dnd.command(aliases=['money' 'ganhos'])
    async def ouro(self, ctx):
        x = discord.Embed(title='**Ouro Inicial**')
        x.set_image(url='https://cdn.discordapp.com/attachments/753004109790969867/853721847496966204/ouro.jpg')
        await ctx.send(embed=x)

    @dnd.command(aliases=['pacote', 'pacotes'])
    async def pct(self, ctx):
        x = discord.Embed(title='**Pacotes**')
        x.set_image(url='https://cdn.discordapp.com/attachments/866686570894196746/876224208512909322/Screenshot_20210724-132835-717.png')
        await ctx.send(embed=x)

def setup(lara):
    lara.add_cog(diversao_cog(lara))