# Archibald bot, Archivist for the Library of Zebulax
import os
import discord
import asyncio
import random
from dotenv import load_dotenv
from CatchPhrases import catchPhrases
from ArchibaldPlays import archibaldPlaying
from ArchibaldQuotes import archibaldQuotes
from ArchibaldAnswers import archibaldAnswers
from ArchibaldDoubt import archibaldDoubt
from ArchibaldPayRespects import archibaldPayRespects
from AutoGnome import limb_loss
from AutoGnome import autoGnome_malfunction
#from libraryPoints import get_name
#from libraryPoints import award_points
#from libraryPoints import revoke_points

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

players = [
        'BARTAVIOUS',
        'JAKESKHAKIS247',
        'PIGEONANON',
        'RANDOMAN',
        'QUINNSKY',
        'CROWBARSDENY',
        'AIRLESSWING'
        ]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    game = discord.Game(archibaldPlaying())
    await client.change_presence(status = discord.Status.online, activity = game);

@client.event
async def on_message(message):
    message_upper = (message.content).upper()
    if message.author == client.user:
        return 

    #WIP
    '''
    if 'LIBRARY POINTS' in message_upper:
        if any(a in message_upper for a in players):        #got it!
            print(a)
        member = message.author
        #print(member.name)
        #await message.channel.send(f' {member.name} has a few library points ')
        get_name(member.name)
    '''
    
    if message_upper.startswith('BDE'):
        bde_item = message.content
        bde_response = "In my experiences as an Archivist, %s is approximately %d%% 'Big Dick Energy', as you say." %(bde_item[4:], random.randint(0, 100))
        await message.channel.send(bde_response)


  elif message_upper.startswith('XYZ'):
        await message.channel.send('How far up (vertically) is the target?')
        height = await client.wait_for("message")
        await message.channel.send('How far away (horizontally) is the target?')
        distance = await client.wait_for("message")
        hypotenuse = math.sqrt(int(height.content)**2 + int(distance.content)**2)
        hypnotenuse_answer = 'The target is %d feet away.' %hypotenuse
        await message.channel.send(hypnotenuse_answer)

    elif 'ANIME' in message_upper:
        anime_response = "Uhg, please remove that swill from the library."
        await message.channel.send(anime_response)

    elif 'AUTOGNOME MALFUNCTION' in message_upper:
        #autoGnome_malfunction()
        await message.channel.send(autoGnome_malfunction())        
        
    if message_upper.endswith('?') and any(x in message_upper for x in catchPhrases):
        answer = random.choice(archibaldAnswers)
        await message.channel.send(answer)

    elif any(x in message_upper for x in catchPhrases):
        response = random.choice(archibaldQuotes)
        await message.channel.send(response)
       

    elif 'F' == message_upper:
        f_response = random.choice(archibaldPayRespects)
        await message.channel.send(f_response)

    elif 'X' == message_upper:
        x_response = random.choice(archibaldDoubt)
        await message.channel.send(x_response)
        
    elif message.content == 'raise-exception':
        raise discord.DiscordException
        
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game(archibaldPlaying())
        await client.change_presence(status = discord.Status.online, activity = game);
        await asyncio.sleep(14400) #4 hours
        
client.loop.create_task(my_background_task())

client.run(token)
