import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, has_permissions, MissingPermissions
import random
import datetime
import asyncio
import json
from bot import get_prefix

class mod_cog(commands.Cog):
    def __init__ (self, lara):
        self.lara = lara

    @commands.command(pass_context=True)
    @has_permissions(administrator=True) #ensure that only administrators can use this command
    async def change(self, ctx, cd): #command: bl!changeprefix ...
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = cd

        with open('prefixes.json', 'w') as f: #writes the new prefix into the .json
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {cd}')
        name=f'{cd}BotBot'

    @commands.command(aliases=['expulsar'])
    @has_permissions(kick_members=True)
    async def kick(self, ctx, membro : discord.Member, *, motivo=None):
        x = discord.Embed(title='**Expulsão**')
        x.add_field(name='*Membro Expulso:*', value=f'{membro.mention}', inline=True)
        x.add_field(name='*Por:*', value=f'{ctx.author.mention}', inline=True)
        x.add_field(name='*Motivo:*', value=f'{motivo}', inline=False)
        x.timestamp = datetime.datetime.utcnow()
        await membro.kick()
        await ctx.send(embed=x)

    @commands.command(aliases=['banir'])
    @has_permissions(ban_members=True)
    async def ban(self, ctx, membro : discord.Member, *, motivo=None):
        x = discord.Embed(title='**Expulsão**')
        x.add_field(name='*Membro Banido:*', value=f'{membro.mention}', inline=True)
        x.add_field(name='*Por:*', value=f'{ctx.author.mention}', inline=True)
        x.add_field(name='*Motivo:*', value=f'{motivo}', inline=False)
        x.timestamp = datetime.datetime.utcnow()
        await membro.ban()
        await ctx.send(embed=x)


    @commands.command(aliases=['add', 'role'])
    @has_permissions(manage_roles=True)
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

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def ola(self, ctx):
        await ctx.send('oi')

def setup(lara):
    lara.add_cog(mod_cog(lara))