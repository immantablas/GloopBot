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
            await ctx.message.author.send(f"You are now enrolled in {role}.")

@client.command()
async def drop(ctx, *args):
    rolelist = ctx.author.roles
    classes = " ".join(args).upper()
    for role in rolelist:
        if role.name == classes:
            await ctx.author.remove_roles(role)
            await ctx.message.author.send(f"You dropped {role}")

@client.command()
@commands.is_owner()
async def rolemenu(ctx):
    message = await ctx.send("React to give yourself a role.\n \n :magnet: : `Physics`\n \n :brain: : `Behavioural Neuroscience` \n \n :test_tube: : `Chemistry` \n \n :atom: : `Biochemistry` \n \n :microscope: : `Biology` \n \n :star: : `Other`")
    emojilist = ["🧲", "🧠", "🧪", "⚛", "🔬", "⭐"]
    for emoji in emojilist:
        await message.add_reaction(emoji)

@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji


    channelID = 799458309501091861
    if reaction.message.channel.id != channelID:
        return

    Physics = discord.utils.get(user.guild.roles, name = "Physics")
    BehavioralNeuroscience = discord.utils.get(user.guild.roles, name = "Behavioral Neuroscience")
    Chemistry = discord.utils.get(user.guild.roles, name = "Chemistry")
    Biochemistry = discord.utils.get(user.guild.roles, name = "Biochemistry")
    Biology = discord.utils.get(user.guild.roles, name = "Biology")
    Others = discord.utils.get(user.guild.roles, name = "Other Programs")

    if user.bot:
        return
    
    if emoji == "🧲":
        await user.add_roles(Physics)
    if emoji == "🧠":
        await user.add_roles(BehavioralNeuroscience)
    if emoji == "🧪":
        await user.add_roles(Chemistry)
    if emoji == "⚛":
        await user.add_roles(Biochemistry)
    if emoji == "🔬":
        await user.add_roles(Biology)
    if emoji == "⭐":
        await user.add_roles(Others)

@client.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji
    guild = await client.fetch_guild(payload.guild_id)
    user = await guild.fetch_member(payload.user_id)
    

    channelID = 799458309501091861
    if payload.channel_id != channelID:
        return

    Physics = discord.utils.get(guild.roles, name = "Physics")
    BehavioralNeuroscience = discord.utils.get(guild.roles, name = "Behavioral Neuroscience")
    Chemistry = discord.utils.get(guild.roles, name = "Chemistry")
    Biochemistry = discord.utils.get(guild.roles, name = "Biochemistry")
    Biology = discord.utils.get(guild.roles, name = "Biology")
    Others = discord.utils.get(guild.roles, name = "Other Programs")

    if user.bot:
        return
    
    if str(emoji) == "🧲":
        await user.remove_roles(Physics)
    if str(emoji) == "🧠":
        await user.remove_roles(BehavioralNeuroscience)
    if str(emoji) == "🧪":
        await user.remove_roles(Chemistry)
    if str(emoji) == "⚛":
        await user.remove_roles(Biochemistry)
    if str(emoji) == "🔬":
        await user.remove_roles(Biology)
    if str(emoji) == "⭐":
        await user.remove_roles(Others)

@client.event
async def on_message(message):
    if "discord.gg" in message.content.lower():
        await message.delete()
        await message.author.send("**Your discord invite was deleted as per the rules of the ConU BIO/BIOCHEM/CHEM server.** \n If you wanted to send a discord invite to a specific individual, feel free to directly message them the invitation.")
        return
    await client.process_commands(message)

@client.event
async def on_message_edit(before, message):
    if "discord.gg" in message.content.lower():
        await message.delete()
        await message.author.send("**Your discord invite was deleted as per the rules of the ConU BIO/BIOCHEM/CHEM server.** \n If you wanted to send a discord invite to a specific individual, feel free to directly message them the invitation.")
        return
    

client.run(SECRET_KEY)