import os

import deepl
from dotenv import load_dotenv
import discord
from discord import *

load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")
DEEPL_KEY = os.environ.get("DEEPL_KEY")

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user}")

@bot.slash_command(description="Do translation.")
async def trans(ctx: ApplicationContext, *, text):
    translator = deepl.Translator(DEEPL_KEY)
    result = translator.translate_text(text, target_lang='JA')
    await ctx.respond(text)
    await ctx.send(result)


bot.run(TOKEN)