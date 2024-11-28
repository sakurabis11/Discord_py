import discord
from discord.ext import commands
from discord import app_commands
import SoraDBlite
from SoraDBlite import SoraDBLiteError, SoraDBlite

clients = ""
dbs = ""
collections = ""

db = SoraDBlite()

db.connect(clients,dbs,collections)

class Dis(commands.Bot):
    async def on_ready(self):

        print(f"{self.user} is now connected!")
        try:
            synced = await client.tree.sync()
            print(f"{len(synced)}")
        except Exception as e:
            print(e)

    async def on_message(self,message):
        if message.author.bot:
            return
        if not message.guild:
            return
        user_id = message.author.id
        user = await client.fetch_user(user_id)
        guildid = message.guild.id
        r_check = db.find_one({"rank_guild_id": guildid})
        if r_check is None:
            pass
        else:
            r_onoff = r_check["rank_isenable"]
            if r_onoff == "off":
                pass
            elif r_onoff == "on":
                r_user = db.find_one({"r_guild_id": guildid,"rank_user_id": user_id})
                if r_user is None:
                    db.insert_one({"r_guild_id": guildid, "rank_user_id": user_id, "r_guild_id": guildid, "msg_count": 1 , "rank": 0})
                else:
                    r_user2 = db.find_one({"r_guild_id": guildid,"rank_user_id": user_id})
                    msgcount = r_user2["msg_count"]
                    filter = {"r_guild_id": guildid,"rank_user_id": user_id}
                    update = {"$set": {"msg_count": msgcount+1}}
                    db.update_one(filter,update)

                    r_user3 = db.find_one({"r_guild_id": guildid,"rank_user_id": user_id})
                    msgcount2 = r_user3["msg_count"]
                    if msgcount2 % 10 ==0:
                        rankcount = r_user3["rank"]
                        filter = {"r_guild_id": guildid,"rank_user_id": user_id}
                        update = {"$set": {"rank": rankcount + 1}}
                        db.update_one(filter , update)
                        channelid = r_check["rank_channel"]
                        r_user4 = db.find_one({"r_guild_id": guildid,"rank_user_id": user_id})
                        rankcount2 = r_user4["rank"]
                        await (client.get_channel(channelid)).send(f"{user.mention} has reached level {rankcount2}. GG!")
                    else:
                        pass
            else:
                pass

intents = discord.Intents.default()
intents.message_content = True
client = Dis(command_prefix="!", intents=intents)

guild_id = discord.Object(1291413928458588200)

@client.tree.command(name="hello", description="Say hello!",guild=guild_id)
async def sayHello(interaction: discord.Interaction):
  try:
    await interaction.response.send_message("Hi there!")
  except Exception as e:
      print(e)

@client.tree.command(name="printer",description="i will print the message you will given",guild=guild_id)
async def sayprint(msg:discord.Interaction,printer:str):
    await msg.response.send_message(printer)

@client.tree.command(name="rankingenable", description="Enabling the ranking system value: on/off")
async def enable(msg:discord.Interaction, on_off:str, channel_id:str):

    guildi_d = msg.guild.id
    u_id = msg.user.id
    onoff = on_off.lower()
    channel_id = int(channel_id)

    guild = client.get_guild(guildi_d)
    chnl = guild.get_channel(channel_id)
    user = await client.fetch_user(u_id)

    if onoff == "on":
        check1 = db.find_one({"rank_guild_id": guildi_d})
        if check1 is None:
            db.insert_one({"rank_guild_id": guildi_d, "user_id":u_id, "rank_isenable": "on", "rank_channel":int(channel_id)})
            check2 = db.find_one({"rank_guild_id": guildi_d})
            if check2:
                await msg.response.send_message(f"Ranking system is enabled the message will send to {chnl.mention} by user: {user.mention}")
            elif check2 is None:
                await msg.response.send_message("Something error occured.")

        else:
            check3 = db.find_one({"rank_guild_id": guildi_d})
            check_onoff1 = check3["rank_isenable"]
            if check_onoff1 == "off":
                filter1 = {"rank_guild_id": guildi_d}
                update1 = {"$set": {"rank_isenable": "on", "rank_channel":int(channel_id)}}
                db.update_one(filter1 , update1)
                await msg.response.send_message(
                    f"Ranking system is enabled the message will send to {chnl.mention} by user: {user.mention}")
            elif check_onoff1 == "on":
                await msg.response.send_message("It is already enable.")

    elif onoff == "off":
        check4 = db.find_one({"rank_guild_id": guildi_d})
        if check4 is None:
            await msg.response.send_message("You didn't enable the ranking system")
        else:
            check5 = db.find_one({"rank_guild_id": guildi_d})
            check_onoff2 = check5["rank_isenable"]
            if check_onoff2 == "on":
                filter2 = {"rank_guild_id": guildi_d}
                update2 = {"$set": {"rank_isenable": "off" , "rank_channel": int(channel_id)}}
                db.update_one(filter2, update2)
                await msg.response.send_message(
                    f"Ranking system is disable by user: {user.mention}")
            elif check_onoff2 == "off":
                await msg.response.send_message("It is already disabled.")

    else:
        await msg.response.send_message("Invalid value, please enter correct value.")

client.run("")
