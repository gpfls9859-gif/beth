import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} 로그인 완료!')

@bot.command()
async def 지원사업(ctx):
    await ctx.send("Beth가 지원사업 링크를 기다리고 있어요!")

bot.run(TOKEN)