import discord
from discord.ext import commands
import random
import datetime
import asyncio
import json

with open('config.json') as e:
    infos = json.load(e)
    prefixo = infos['prefix']

class mod_cog(commands.Cog):
    def __init__ (self, lara):
        self.lara = lara

    @commands.command(aliases=['expulsar'])
    async def kick(self, ctx, membro : discord.Member, *, motivo=None):
        x = discord.Embed(title='**Expulsão**')
        x.add_field(name='*Membro Expulso:*', value=f'{membro.mention}', inline=True)
        x.add_field(name='*Por:*', value=f'{ctx.author.mention}', inline=True)
        x.add_field(name='*Motivo:*', value=f'{motivo}', inline=False)
        x.timestamp = datetime.datetime.utcnow()
        await membro.kick()
        await ctx.send(embed=x)


    @commands.command(aliases=['banir'])
    async def ban(self, ctx, membro : discord.Member, *, motivo=None):
        x = discord.Embed(title='**Expulsão**')
        x.add_field(name='*Membro Banido:*', value=f'{membro.mention}', inline=True)
        x.add_field(name='*Por:*', value=f'{ctx.author.mention}', inline=True)
        x.add_field(name='*Motivo:*', value=f'{motivo}', inline=False)
        x.timestamp = datetime.datetime.utcnow()
        await membro.ban()
        await ctx.send(embed=x)


    @commands.command(aliases=['add', 'role'])
    async def cargo(self, ctx, user : discord.Member, cargo : discord.Role):
        await user.add_roles(cargo)
        x = discord.Embed(title='Cargo adicionado!')
        x.add_field(name='**Membro:**', value=user.mention, inline=False)
        x.add_field(name='*Cargo adicionado:*', value=cargo.mention, inline=False)
        x.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        x.timestamp = datetime.datetime.utcnow()
        x.set_thumbnail(url=ctx.guild.icon_url)
        msg = await ctx.send(embed=x)
        await msg.add_reaction('✅')

def setup(lara):
    lara.add_cog(mod_cog(lara))