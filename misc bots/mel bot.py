import discord
import random
from asd import *
client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    
@client.event
async def on_message(message):
    message.content = message.content.lower()
    message.content = message.content.replace(" ","")
    try:
        if "mel" in message.content:
            
            message.content = message.content.replace("mel ", "")
            
            embed=discord.Embed(title= melble()[:255] , color=0x2A7949)
            embed.set_author(name="From the Book of {}".format(message.content))
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/662435501227245571/662442459057356839/IMG_1254.jpg?width=419&height=559")
            await message.channel.send(embed=embed)       
    except:
        embed=discord.Embed(title= "Please try again nerd" , color=0x2A7949)
        embed.set_author(name="That was an invalid passage".format(message.content))
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/662435501227245571/662442459057356839/IMG_1254.jpg?width=419&height=559")
        await message.channel.send(embed=embed)              
        

client.run('NjYyNTAzMjU5NDU3NTg1MTY0.Xg67YQ.8-OdEoADRMA3lO-RaA10naXCa1Q') 

def fromFile(fileName):
    f = open("{}.txt".format(fileName), "r")
    return f.readlines()
    