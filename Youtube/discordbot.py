# Imports
import discord
from discord import app_commands
from discord.ext import commands
import requests
from config import token, apikey

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
@bot.tree.command(name='𝐋𝐎𝐎𝐊 𝐁𝐎𝐓 𝐎𝐒𝐈𝐍𝐓', description='🔎🤖 Bot OSINT Discord simple et rapide
Il aide à rechercher et analyser des infos publiques sur des personnes, pseudos et sites web 🌐📊
⚡ Ultra pratique, léger et facile à utiliser
🛡️ Respecte les bonnes pratiques et les sources ouvertes'


# Bot Prompt, API Call, and Response Functionality
@app_commands.describe(user_input) = "entrer une aresse ip"
async def 𝐋𝐎𝐎𝐊 𝐁𝐎𝐓 𝐎𝐒𝐈𝐍𝐓 (interaction: discord.Interaction, user_input: str):                 

    # Use Requests to Obtain Data from API
    url = f'https://api.ipgeolocation.io/ipgeo?apiKey={apikey}**Input Variable***{user_input}'
    response = requests.get(url)
    json_response = response.json()

    # Send Message Containing Requested Data to User
    await interaction.response.send_message(f'IP :{ json_reponse = (ip)}' /nContry {json_reponse('contry name')} /nISP: {json_reponse('ISP')}, ephemeral=True)
    return

bot.run(token) # Run Bot
