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
    if message.content.startswith("~Idea"):
        embed=discord.Embed(title= startUp() , color=0x7BAA47)
        embed.set_author(name="HOLY FUCK DUDE I GOT AN IDEA")
        embed.set_thumbnail(url="https://media.tenor.com/images/a32b1c862f8ffb730ba22fda8076c82c/tenor.gif")
        await message.channel.send(embed=embed)        
        

client.run('NjI4MDcyMjA0MTk3NjkxMzkz.XZF4Fg.BQ7LSMteJ0p54tSZi9sJkfZSrdc') 