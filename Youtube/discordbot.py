# Imports
import discord
from discord import app_commands
from discord.ext import commands
import requests
from config import token, api
# Bot Configuration
intents = discord.Intents.default() 
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='/')

#Sync
@bot.event
async def on_ready():
    await bot.tree.sync()
    print('Bot is running and has synced.')

# Establish Command Name and Description 
@bot.tree.command(name='Lookbot ip', description='Lookup bot for ip')

# Bot Prompt, API Call, and Response Functionality
@app_commands.describe(user_input = "Please enter a IP adress ")                 # Prompt User for Input
async def ip_lookup(interaction: discord.Interaction, user_input: str):                 

    # Use Requests to Obtain Data from API
    url = f'https://api.ipgeolocation.io/v3/ipgeo?apiKey=API_KEY&ip=91.128.103.196'{apikey}***Input Variable***{user_input}'
    response = requests.get(url)
    json_response = response.json()

    # Send Message Containing Requested Data to User
    await interaction.response.send_message(f'IP:{json_reponse("ip")}/nCountry:{json_reponse("country name")}/nISP:{json_reponse("isp")}True)
    return

bot.run(token) # Run Bot
