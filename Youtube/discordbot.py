import discord
from discord import app_commands
from discord.ext import commands
import requests
from config import token, apikey

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot connecté et prêt")

@bot.tree.command(
    name="LOOK BOT OSINT",
    description="Bot OSINT simple pour analyser une IP"
)
@app_commands.describe(
    user_input="Entrez une adresse IP"
)
async def lookup(interaction: discord.Interaction, user_input: str):

    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={apikey}&ip={user_input}"
    response = requests.get(url)
    data = response.json()

    await interaction.response.send_message(
        f"🌍 IP : {data.get('ip')}\n"
        f"📍 Pays : {data.get('country_name')}\n"
        f"🏢 ISP : {data.get('isp')}",
        ephemeral=True
    )

bot.run(token)
