import disnake, io, requests, json, asyncio, datetime, random, os, psutil, openai, traceback, calendar, aiohttp
from disnake.ext import commands

async def requisitar(tipo):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://nekos.life/api/v2/img/{tipo}') as response:
            data = await response.json()
            imgs = data['url']
            return imgs

async def send_message_chunks(channel, message, caixa=None, imgs : str =None):
    max_length=1500
    if caixa is None:
        chunks = [message[i:i+max_length] for i in range(0, len(message), max_length)]
        for chunk in chunks:
            await channel.send(chunk)
    else:
        for i, chunk in enumerate(message[i:i+max_length] for i in range(0, len(message), max_length)):
            x = disnake.Embed(title=f'{caixa} (parte {i+1})', description=chunk)
            if imgs != None:
                x.set_thumbnail(url=f'{imgs}')
            await channel.send(embed=x)



#arquivo de multi-funções