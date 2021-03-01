import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
SECRET_KEY = os.getenv("TOKEN")

client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
    print('bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command()
@commands.is_owner()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

@client.command()
async def enroll(ctx, *args):
    rolelist = ctx.guild.roles
    classes = " ".join(args).upper()
    for role in rolelist:
        if role.name == classes:
            await ctx.author.add_roles(role)
            await ctx.send(f"You are now enrolled in {role}.")

@client.command()
async def drop(ctx, *args):
    rolelist = ctx.author.roles
    classes = " ".join(args).upper()
    for role in rolelist:
        if role.name == classes:
            await ctx.author.remove_roles(role)
            await ctx.send(f"You dropped {role}")



client.run(SECRET_KEY)
