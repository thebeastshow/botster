import discord
import json

from discord.ext import commands
from discord.utils import get

###################################################
# Botster - A lovely little Discord Bot           #
# ----------------------------------------------- #
# @author Otis Anderson - busterstopit@gmail.com  #
###################################################

bot = commands.Bot(command_prefix='$')
busterEmotes = ["snoot", "party", "mrbuster", "atac", "booster", "busted"]

#load config file
with open('botconfig.json') as json_data_file:
	config = json.load(json_data_file)
	
updateFile = config["updateFile"]
updateChannel = config["updateChannel"]

###########################
# BOTSTER COMMAND SECTION #
###########################
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Botster", description="A little bot named Botster.", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="OtIs")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)
	
###########################
#  BOTSTER EVENT SECTION  #
###########################	
@bot.event
async def on_message(message):
	# message in current-caller channel?
	if message.channel.name == updateChannel:
		print("New Update:\n" + message.content)
		
		#Write the message to a file
		with open(updateFile,'r+') as f:
			#convert to string:
			data = f.read()
			
			f.seek(0)
			f.write(message.content)
			f.truncate()
			f.close()
			
	# Add emoji's based on key words
	txt = message.content.lower()		
	if 'buster' in txt:
		for emote in busterEmotes:
			emoji = get(bot.get_all_emojis(), name=emote)
			await bot.add_reaction(message, emoji)
			
	if 'otis' in txt:
		emoji = get(bot.get_all_emojis(), name='otis')
		await bot.add_reaction(message, emoji)
		
	if 'john' in txt:
		emoji = get(bot.get_all_emojis(), name='goof')
		await bot.add_reaction(message, emoji)
		
	if 'best' in txt:
		emoji = get(bot.get_all_emojis(), name='best1')
		await bot.add_reaction(message, emoji)
		

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Botster", description="A little bot named Botster. List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('NDg5OTU1MTE4MjQyODU2OTcw.DnySog.JElGYdtKyGXLFhNXD9fetZmxLVY')