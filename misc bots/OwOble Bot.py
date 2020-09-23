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
        if message.content.startswith("mel"):
            
            message.content = message.content.replace("mel ", "")
            
            embed=discord.Embed(title= OwOBle(message.content)[:255] , color=0x2A7949)
            embed.set_author(name="From the Book of {}".format(message.content))
            embed.set_thumbnail(url="https://files.catbox.moe/90gq18.PNG")
            await message.channel.send(embed=embed)       
    except:
        embed=discord.Embed(title= "Please try again nerd" , color=0x2A7949)
        embed.set_author(name="That was an invalid passage".format(message.content))
        embed.set_thumbnail(url="https://files.catbox.moe/90gq18.PNG")
        await message.channel.send(embed=embed)              
        

client.run('NjI4MDgxNDI2MjE4MzUyNjUw.XZGCYA.H1ZUvRE_JPnKQ2T_hb9ypAuXV0c') 