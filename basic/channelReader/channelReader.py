import discord
import json

from discord.ext import commands


###################################################
# channelReader - A lovely little Discord Bot     #
#                                                 # 
# Function: Copies text from a specified Discord  #
#           channel and outputs it to a text file #
# ----------------------------------------------- #
# @author Otis Anderson - busterstopit@gmail.com  #
###################################################

bot = commands.Bot(command_prefix='$!@#')

#load config file
with open('botconfig.json') as json_data_file:
	config = json.load(json_data_file)
	
updateFile = config["updateFile"]
updateChannel = config["updateChannel"]
token = config["token"]


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
	
###########################
#    BOT EVENT SECTION    #
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
			# output to file
			f.seek(0)
			f.write(message.content)
			f.truncate()
			f.close()
		

bot.run(token)