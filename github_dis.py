import discord 
from discord.ext import commands
from discord import app_commands

import SoraDBlite 
from SoraDBlite import SoraDBlite, SoraDBLiteError

class disc(Commands.Bot):
  

intents = discord.Intents.default()
intents.message_content = True
client = disc(command_prefix="!", intents=intents)

guild_id = discord.Object(1291413928458588200)

@client.tree.command(name="add_github", description="just add your link of the github repo", guild=guild_id)
async def addgithub(msg:discord.Interaction, link:str, channelid:str):
  
