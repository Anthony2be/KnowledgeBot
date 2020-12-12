import discord
from discord.ext import commands

import urllib.request
import json
import time
import os
from datetime import datetime

# Discord stuff
token = open("token.txt",mode="r")
bot = commands.Bot(command_prefix='^')

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

@bot.event
async def on_ready():
    print("Connected!")

bot.run(token.read())
