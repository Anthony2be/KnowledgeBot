import discord
from discord.ext import commands

import urllib.request
import json
import time
import os
from datetime import datetime

# Discord stuff
if os.path.isfile('prefixes.json') == False:
    with open('prefixes.json', 'w') as f:
        json.dump({}, f)
        f.close()

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix)

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '^'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 2)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 2)


token = open("token.txt",mode="r")


# Global variables
branch = "main"
latestTree = {}

# Bot command declarations
@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! Latency: `'+str(round(bot.latency*1000))+"ms`")

@bot.group()
async def admin(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Subcommand pls.")

@admin.command()
async def disconnect(ctx):
    await bot.close()

@bot.command(brief = 'Changes the bot\'s prefix', description = 'Changes the bot\'s prefix for the server')
@commands.has_permissions(administrator = True)
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 2)
    await ctx.send('Changed the prefix to `' + prefix + '`')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)

@bot.event
async def on_ready():
    print("Connected!")



bot.run(token.read())