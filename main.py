import discord
from discord.ext import commands
import os

token = ""
serverOn = False

intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    activity = discord.Game(name="Serving Server")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"Logged in as {bot.user}")

@bot.command()
async def startServer(ctx):
    global serverOn
    if not serverOn:
        ctx.send("Starting server")
        serverOn = True
        os.system("start.bat")
        ctx.send("Rip server")
        serverOn = False

bot.run(token)