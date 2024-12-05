import discord 
from discord.ext import commands
from discord import app_commands

import SoraDBlite 
from SoraDBlite import SoraDBlite, SoraDBLiteError

m_uri = ""
m_password = ""
m_collection = ""

db = SoraDBlite()

db.connect(m_uri, m_password, m_collection)

class disc(Commands.Bot):

intents = discord.Intents.default()
intents.message_content = True
client = disc(command_prefix="!", intents=intents)

guild_id = discord.Object(1291413928458588200)

@client.tree.command(name="add_github", description="just add your link of the github repo", guild=guild_id)
async def addgithub(msg:discord.Interaction, link:str, channelid:str):
  guildi_d = msg.guild.id
    u_id = msg.user.id
    onoff = on_off.lower()
    channel_id = int(channel_id)

    guild = client.get_guild(guildi_d)
    chnl = guild.get_channel(channel_id)
    user = await client.fetch_user(u_id)

  
