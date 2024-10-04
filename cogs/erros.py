import discord, traceback, asyncio, datetime
from discord.ext import commands


class Erros(commands.Cog):

    def __init__(self, lara):
        self.lara = lara
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if ctx.author.id == self.lara.owner_id:
            if isinstance(error, commands.errors.CommandError):
                o_erro = f'Ocorreu um erro ao executar o comando: {str(error)}\n Causa: {commands.errors.CommandError}'
            else:
                # Obtém informações detalhadas do traceback do erro
                error_traceback = traceback.format_exception(type(error), error, error.__traceback__)
                error_message = ''.join(error_traceback)
                o_erro = f'Ocorreu um erro inesperado:\n```{error_message}```'
            msg = discord.Embed(title=f'Desenvolvedor!', description=f'{o_erro}', color=0xff0000)
        else:

            if isinstance(error, commands.CommandNotFound):
                msg = discord.Embed(title=f'Comando não encontrado', description=f'Desculpe-me mas, o comando não foi encontrado!\nVerifique se digitou o comando corretamente.', color=0xff0000)

            elif isinstance(error, commands.MissingPermissions):
                msg = discord.Embed(title=f'Permissão não atribuída!', description=f'Você não possue permissão para executar essa função!', color=0xff0000)

            elif isinstance(error, commands.CommandOnCooldown):
                msg = discord.Embed(title=f'Calma ae bro!',description=f'tente denovo em: {int(error.retry_after)}s.', color=0xff0000)

            elif isinstance(error, commands.UserInputError):
                msg = discord.Embed(title=f'Erro de entrada!', description=f'Por favor, coloque a informação pedida!', color=0xff0000)

            else:
                msg = discord.Embed(title=f'Erro!', description=f'Comando não pode ser executado!', color=0xff0000)

        msg.set_footer(text=f'{self.lara.user}', icon_url=self.lara.user.avatar)
        mess_er = await ctx.send(embed=msg)
        await mess_er.add_reaction("✅")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "✅"

        try:
            reaction, _ = await self.lara.wait_for("reaction_add", check=check, timeout=10.0)
            await mess_er.delete()
            await ctx.message.delete()
        except TimeoutError:
            await ctx.send("Tempo limite atingido. Ação cancelada.", delete_after=3)
            await asyncio.sleep(5)
            await mess_er.delete()
            await ctx.message.delete()
            

def setup(lara):
    lara.add_cog(Erros(lara))
