# bot.py
import os

import discord
from dotenv import load_dotenv
import random

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(name=f'Hello', help='Responds with a greeting from Normal_Man_Bot')
async def greeting(ctx):
    await ctx.send(f"Hello, {ctx.message.author.mention}\nMy name is {bot.user.name}!")



@bot.command(name='create-channel', channel_name='test-channel')
@commands.has_role('Ruler')
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


bot.run(TOKEN)

# intents = discord.Intents.all()
# client = discord.Client(intents=intents)


# @client.event
# async def on_ready():
#     guild = discord.utils.get(client.guilds, name=GUILD)
#     print(f'{client.user.name} has connected to Discord!')
#
#
# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(f"Hi {member.name}, welcome to {discord.utils.get(client.guilds, name=GUILD)}")
#
#
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     brooklyn_99_quotes = [
#         "I'm the human form of the 💯 emoji.",
#         "Bingpot!",
#         (
#             "Cool. Cool cool cool cool cool cool cool, "
#             "no doubt no doubt no doubt no doubt."
#         ),
#         "\*Gives you Reddit Gold with a grin, blushes\*"
#
#     ]
#
#     if message.content == '99!':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)
#     elif f'ty bot' in message.content:
#         await message.channel.send("No, thank YOU. I work very hard but alas, I am just a bot...")
#     elif message.content == 'raise-exception':
#         await message.channel.send(f"{message.author.name}, why must you do this to me?")
#         raise discord.DiscordException
#
#
# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise
#
#
# client.run(TOKEN)

