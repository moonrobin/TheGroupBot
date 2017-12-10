import discord
import asyncio
from random import *
client = discord.Client()
boards = []


class Board:
    def __init__(self, name, e1, e2, e3, boss):
        self.n = name
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        self.b = boss

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    global boards
    boards.append(Board('Practice Field', 'Random', 'Random', 'Random', ''))
    boards.append(Board('Space Wanderer', 'Random', 'Random', 'Random', ''))
    boards.append(Board('Pudding Chase', 'Minelayer', 'Random', 'Random', 'Store Manager'))
    boards.append(Board('Christmas Miracle', 'Miracle', 'Random', 'Random', 'Store Manager'))
    boards.append(Board('Lagoon Flight', 'Charity', 'Random', 'Random', 'Flying Castle'))
    boards.append(Board('Planet Earth', 'Regeneration', 'Random', 'Random', 'Shifu Robot'))
    boards.append(Board('Warfare', 'Air Raid', 'Random', 'Random', 'Shifu Robot'))
    boards.append(Board('Highway Heist', 'Charity', 'Minelayer', 'Battlefield', 'Store Manager'))
    boards.append(Board('Sealed Archive', 'Regeneration', 'Minelayer', 'Battlefield', 'Shifu Robot'))
    boards.append(Board('Sunset', 'Charity', 'Minelayer', 'Miracle', 'Flying Castle'))
    boards.append(Board('Tomomo\'s Abyss', 'Battlefield', 'Random', 'Random', 'Store Manager'))
    boards.append(Board('White Winter', 'Charity', 'Freeze', 'Random', 'Store Manager'))
    boards.append(Board('Clover', 'Miracle', 'Backtrack', 'Random', 'Shifu Robot'))
    boards.append(Board('Night Flight', 'Regeneration', 'Confusion', 'Random', 'Flying Castle'))
    boards.append(Board('Farm', 'Confusion', 'Backtrack', 'Random', 'Store Manager'))
    boards.append(Board('Star Circuit', 'Sprint', 'Home Roulette', 'Random', 'Shifu Robot'))
    boards.append(Board('Training Program', 'Regeneration', 'Sprint', 'Random', 'Shifu Robot'))
    boards.append(Board('Vortex', 'Bomber', 'Battlefield', 'Random', 'Shifu Robot'))
    boards.append(Board('Sweet Heaven', 'Confusion', 'Miracle', 'Random', 'Store Manager'))
    boards.append(Board('Starship', 'Mystery', 'Home Roulette', 'Random', 'Store Manager'))
    boards.append(Board('Frost Cave', 'Freeze', 'Backtrack', 'Random', 'Flying Castle'))
    boards.append(Board('Shipyard', 'Mystery', 'Bomber', 'Home Roulette', 'Shifu Robot'))
    boards.append(Board('Treasure Island', 'Treasure', 'Amplify', 'Random', 'Store Manager'))
    boards.append(Board('Treasure Island (Night)', 'Amplify', 'Battlefield', 'Minelayer', 'Store Manager'))
    boards.append(Board('Witch Forest', 'Home Roulette', 'Mystery', 'Random', 'Flying Castle'))

    print('boards loaded')
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!rollboard') or message.content.startswith('!rb'):
        global boards
        index = randint(0, len(boards) - 1)
        board = boards[index]
        output = '**{}**\n\n__Events__\n  1.  {}\n  2. {}\n  3. {}\n\n__Boss__\n  {}'.format(board.n, board.e1, board.e2, board.e3, board.b)
        await client.send_message(message.channel, output)

client.run('') # TODO: Insert Token here