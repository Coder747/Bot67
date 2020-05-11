import discord
import os                          
from discord.ext import commands
import random




client = commands.Bot(command_prefix = '.')     #prefix before issuing commands

#Events
@client.event                                  
async def on_ready():                           #when the bot is online
    print("Online")

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server people.")
    await channel.send_message(f"{member} has joined the server people.")


@client.event
async def on_member_remove(member):
    print(f"{member} has dissappeared.")
    await channel.send_message(f"{member} has dissappeared.")

#-------------------------------------------------------------------------------------------------------   
#Commands
@client.command()
async def ping(ctx):        #ping is the command name (ie. /ping)
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms")

@client.command(aliases=['8ball'])  #/8ball is == _8ball
async def _8ball(ctx):
    responses =["As I see it, yes.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don’t count on it.",
                "It is certain.",
                "It is decidedly so.",
                "Most likely.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Outlook good.",
                "Reply hazy, try again.",
                "Signs point to yes.",
                "Very doubtful.",
                "Without a doubt.",
                "Yes.",
                "Yes, definitely.",
                "You may rely on it."]
    await ctx.send(f"{random.choice(responses)}")


@client.command()
async def clear(ctx,amount = 5):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f"Deleted {amount} messages.")

@client.command
async def kick(ctx, member : discord.Member, * ,reason=None):    #all parameters passed after member and reason will be added to reason  
    await member.kick(reason=reason)


key = os.environ.get('botkey')
client.run(key)   #run the bot
