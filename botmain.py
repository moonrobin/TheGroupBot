import discord
import asyncio
from random import *
client = discord.Client()
boards = []


class Board:
    def __init__(self, name, e1, e2, e3, boss, image):
        self.n = name
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        self.b = boss
        self.i = image

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    global boards
    boards.append(Board('Practice Field', 'Random', 'Random', 'Random', '', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/c/c0/Practicefield.png'))
    boards.append(Board('Space Wanderer', 'Random', 'Random', 'Random', '', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/e/e1/Spacewander.png'))
    boards.append(Board('Pudding Chase', 'Minelayer', 'Random', 'Random', 'Store Manager', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/c/c2/Puddingchase.png'))
    boards.append(Board('Christmas Miracle', 'Miracle', 'Random', 'Random', 'Store Manager', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/2/21/Christmasmiracle.png'))
    boards.append(Board('Lagoon Flight', 'Charity', 'Random', 'Random', 'Flying Castle', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/c/c5/Lagoon_Flight.png'))
    boards.append(Board('Planet Earth', 'Regeneration', 'Random', 'Random', 'Shifu Robot', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/d/de/Planet_earth.jpg'))
    boards.append(Board('Warfare', 'Air Raid', 'Random', 'Random', 'Shifu Robot', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/4/44/Warfare.png'))
    boards.append(Board('Highway Heist', 'Charity', 'Minelayer', 'Battlefield', 'Store Manager', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/a/a4/Highwayheist.png'))
    boards.append(Board('Sealed Archive', 'Regeneration', 'Minelayer', 'Battlefield', 'Shifu Robot', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/8/8e/Sealedarchive.png'))
    boards.append(Board('Sunset', 'Charity', 'Minelayer', 'Miracle', 'Flying Castle', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/4/47/Sunset.png'))
    boards.append(Board('Tomomo\'s Abyss', 'Battlefield', 'Random', 'Random', 'Store Manager', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/b/ba/Tomomosabyss.png'))
    boards.append(Board('White Winter', 'Charity', 'Freeze', 'Random', 'Store Manager', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/7/76/White_winter.jpg'))
    boards.append(Board('Clover', 'Miracle', 'Backtrack', 'Random', 'Shifu Robot', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/5/58/Clover.jpeg'))
    boards.append(Board('Night Flight', 'Regeneration', 'Confusion', 'Random', 'Flying Castle', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/6/6f/Night_Flight.jpeg'))
    boards.append(Board('Farm', 'Confusion', 'Backtrack', 'Random', 'Store Manager', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/b/b9/Farm.jpeg'))
    boards.append(Board('Star Circuit', 'Sprint', 'Home Roulette', 'Random', 'Shifu Robot', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/7/7a/Star_circuit.PNG'))
    boards.append(Board('Training Program', 'Regeneration', 'Sprint', 'Random', 'Shifu Robot', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/f/fd/Trainingprogram.jpg'))
    boards.append(Board('Vortex', 'Bomber', 'Battlefield', 'Random', 'Shifu Robot', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/5/52/Vortex.png'))
    boards.append(Board('Sweet Heaven', 'Confusion', 'Miracle', 'Random', 'Store Manager', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/a/a8/Sweet_Heaven.png'))
    boards.append(Board('Starship', 'Mystery', 'Home Roulette', 'Random', 'Store Manager', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/7/7d/Starship.png'))
    boards.append(Board('Frost Cave', 'Freeze', 'Backtrack', 'Random', 'Flying Castle', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/6/65/Frost_Cave.jpg'))
    boards.append(Board('Shipyard', 'Mystery', 'Bomber', 'Home Roulette', 'Shifu Robot', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/0/0f/Shipyard.png'))
    boards.append(Board('Treasure Island', 'Treasure', 'Amplify', 'Random', 'Store Manager', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/3/3d/Treasure_Island.PNG'))
    boards.append(Board('Treasure Island (Night)', 'Amplify', 'Battlefield', 'Minelayer', 'Store Manager', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/3/3d/Treasure_Island_%28Night%29.PNG'))
    boards.append(Board('Witch Forest', 'Home Roulette', 'Mystery', 'Random', 'Flying Castle', 'https://vignette.wikia.nocookie.net/onehundredpercentorangejuice/images/7/7f/Witch_Forest.png'))

    print('boards loaded')
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!rollboard') or message.content.startswith('!rb'):
        global boards
        index = randint(0, len(boards) - 1)
        board = boards[index]
        map_output = '**{}**\n{}'.format(board.n, board.i)
        await client.send_message(message.channel, map_output)
        event_output = '\n\n__Events__\n  1.  {}\n  2. {}\n  3. {}\n\n__Boss__\n  {}'.format(board.e1, board.e2, board.e3, board.b)
        await client.send_message(message.channel, event_output)

client.run('Mzg4MTY5NTE4MjMwNTM2MjAy.DQ5eSA.ngZILefR9YjwqCjA4tCthlPI8D8') # TODO: Insert Token here