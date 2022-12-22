import os
from dotenv import load_dotenv
from discord import *

load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")
DEEPL_KEY = os.environ.get("DEEPL_KEY")

bot = discord.Bot()
