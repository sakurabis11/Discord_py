import discord
import SoraDBlite
from SoraDBlite import SoraDBLiteError, SoraDBlite

clients = "mongodb+srv://o53317853:vvgvjhjhvjh@cluster0.aerrmcs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
dbs = "vvgvjhjhvjh"
collections = "asdiemkd"
GUILD_ID = 1258871266098548888

db = SoraDBlite()

db.connect(clients,dbs,collections)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

log_ch_id = 1294291782364041377

async def get_logs(guild):
    return guild.get_channel(log_ch_id)

@client.event
async def on_message(message):
    try:
        if message.author.bot:
            return
        if message.guild.id != GUILD_ID:
            return
        user_id = message.author.id
        user = await client.fetch_user(user_id)
        search_id = db.find_one({"userid": user_id})
        if search_id is None:
            db.insert_one({"userid": user_id , "msg_count": 1})
            search_id2 = db.find_one({"userid": user_id})
            msgcount2 = search_id2["msg_count"]
            await (client.get_channel(log_ch_id)).send(f"{user.mention} has been increased rank.\nRank: {msgcount2}")
        else:
            msgcount = search_id["msg_count"]
            filter = {"userid": user_id}
            update = {"$set": {"msg_count": msgcount + 1}}
            x = db.update_one(filter , update)
            if x:
                search_id3 = db.find_one({"userid": user_id})
                msgcount1 = search_id3["msg_count"]
                await (client.get_channel(log_ch_id)).send(
                    f"{user.mention} has been increased rank.\nRank: {msgcount1}")
            else:
                await (client.get_channel(log_ch_id)).send("Something error occured.")

    except Exception as e:
        print(e)
        db.sora_ai(e)

@client.event
async def on_message(message):
    try:
        if message.author.bot:
            return 
        if message.guild.id!=GUILD_ID:
            return
        if message.startswith('myrank'):
            user_id = message.author.id
            user = await client.fetch_user(user_id)
            search_id = db.find_one({"userid": user_id})
            if search_id is None:
                await (client.get_channel(log_ch_id)).send(f"{user.mention} you have no rank.")
            else:
                msg_count = search_id["msg_count"]
                await (client.get_channel(log_ch_id)).send(f"{user.mention} your rank: {msg_count}")
    except Exception as e:
        print(e)
                

token = ""

client.run(token)
