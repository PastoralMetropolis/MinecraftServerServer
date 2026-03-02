import discord
from discord.ext import commands
import subprocess
import os

token = os.getenv("DISCORD_TOKEN")
launchCommand = "java -jar server.jar nogui"

server_process = None

intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    activity = discord.Game(name="Serving Server")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"Logged in as {bot.user}")
@bot.command()
async def start_server(ctx):
    allowed_guild_id = 1383872929397473370

    if ctx.guild is None or ctx.guild.id != allowed_guild_id:
        return

    global server_process

    if server_process is None or server_process.poll() is not None:
        await ctx.send("Starting server")
        server_process = subprocess.Popen(launchCommand.split())
    else:
        await ctx.send("Server already running")

bot.run(token)