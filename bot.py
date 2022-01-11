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
    message = await ctx.send("React to give yourself a role.\n \n :magnet: : `Physics`\n \n :brain: : `Behavioural Neuroscience` \n \n :test_tube: : `Chemistry` \n \n :atom: : `Biochemistry` \n \n :microscope: : `Biology` \n \n :microbe: : `Cell and Molecular Biology` \n \n :deciduous_tree: : `Ecology` \n \n :computer: : `Systems and Information Biology` \n \n :thinking: : `Psychology` \n \n :muscle: : `Health, Kinesiology, and Applied Physiology` \n \n :earth_americas: : `Geography, Planning and Environment` \n \n :star: : `Other`")
    emojilist = ["🧲", "🧠", "🧪", "⚛", "🔬", "🦠", "🌳", "💻", "🤔", "💪", "🌎", "⭐"]
    for emoji in emojilist:
        await message.add_reaction(emoji)

@client.command()
@commands.is_owner()
async def msg(ctx, user:discord.User, *, text:str):
    await ctx.message.author.send(text)


@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji


    channelID = 852692727107289129
    if reaction.message.channel.id != channelID:
        return

    Physics = discord.utils.get(user.guild.roles, name = "Physics")
    BehavioralNeuroscience = discord.utils.get(user.guild.roles, name = "Behavioral Neuroscience")
    Chemistry = discord.utils.get(user.guild.roles, name = "Chemistry")
    Biochemistry = discord.utils.get(user.guild.roles, name = "Biochemistry")
    Biology = discord.utils.get(user.guild.roles, name = "Biology")
    Cellbio = discord.utils.get(user.guild.roles, name = "Cell and Molecular Biology")
    Ecology = discord.utils.get(user.guild.roles, name = "Ecology")
    Infobio = discord.utils.get(user.guild.roles, name = "Systems and Information Biology")
    Psychology = discord.utils.get(user.guild.roles, name = "Psychology")
    Exci = discord.utils.get(user.guild.roles, name = "Health, Kinesiology, and Applied Physiology")
    Geography = discord.utils.get(user.guild.roles, name = "Geography, Planning and Environment")
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
    if emoji == "🦠":
        await user.add_roles(Cellbio)
    if emoji == "🌳":
        await user.add_roles(Ecology)
    if emoji == "💻":
        await user.add_roles(Infobio)
    if emoji == "🤔":
        await user.add_roles(Psychology)
    if emoji == "💪":
        await user.add_roles(Exci)
    if emoji == "🌎":
        await user.add_roles(Geography)
    if emoji == "⭐":
        await user.add_roles(Others)

@client.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji
    guild = await client.fetch_guild(payload.guild_id)
    user = await guild.fetch_member(payload.user_id)
    

    channelID = 852692727107289129
    if payload.channel_id != channelID:
        return

    Physics = discord.utils.get(guild.roles, name = "Physics")
    BehavioralNeuroscience = discord.utils.get(guild.roles, name = "Behavioral Neuroscience")
    Chemistry = discord.utils.get(guild.roles, name = "Chemistry")
    Biochemistry = discord.utils.get(guild.roles, name = "Biochemistry")
    Biology = discord.utils.get(guild.roles, name = "Biology")
    Cellbio = discord.utils.get(guild.roles, name = "Cell and Molecular Biology")
    Ecology = discord.utils.get(guild.roles, name = "Ecology")
    Infobio = discord.utils.get(guild.roles, name = "Systems and Information Biology")
    Psychology = discord.utils.get(guild.roles, name = "Psychology")
    Exci = discord.utils.get(guild.roles, name = "Health, Kinesiology, and Applied Physiology")
    Geography = discord.utils.get(guild.roles, name = "Geography, Planning and Environment")
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
    if str(emoji) == "🦠":
        await user.remove_roles(Cellbio)
    if str(emoji) == "🌳":
        await user.remove_roles(Ecology)
    if str(emoji) == "💻":
        await user.remove_roles(Infobio)
    if str(emoji) == "🤔":
        await user.remove_roles(Psychology)
    if str(emoji) == "💪":
        await user.remove_roles(Exci)
    if str(emoji) == "🌎":
        await user.remove_roles(Geography)
    if str(emoji) == "⭐":
        await user.remove_roles(Others)

botmessage = "**Your invitation was deleted as per the rules of the ConU BIO/BIOCHEM/CHEM server.** \n If you wanted to send an invite to a specific individual, feel free to directly message them the invitation. This is done to avoid decisions regarding linking back to other groups to ensure that we're providing links to groups that adhere to Concordia's and Discord's guidelines and TOS."

links=["discord.gg", "chat.whatsapp.com", "bit.ly", "goo.gl", "tinyurl.com", "ow.ly"]
@client.event
async def on_message(message):
    for l in links:
        if (l in message.content.lower()):
            await message.delete()
            await message.author.send(botmessage)
            return
    await client.process_commands(message)

@client.event
async def on_message_edit(before, message):
     for l in links:
        if (l in message.content.lower()):
            await message.delete()
            await message.author.send(botmessage)
            return



client.run(SECRET_KEY)