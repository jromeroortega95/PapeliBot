import random
import discord
from discord.ext import commands
from  game.papeligame import PapeliGame


@commands.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes) 
    await ctx.send(response)

@commands.command(name='roll_dice', help='Simulates rolling dice.')
@commands.has_role('admin_bis')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

#Se le pondrá pasar dos parámetros opcionales
#@nombre: Nombre del juego
@commands.command(name='create_game', help='Inicia el bot en el canal del grupo')
async def create_game(ctx, nombre):

    juego = PapeliGame(nombre)
    
    response = 'Se ha creado el juego  '  + nombre 
    await ctx.send(response)

#@palabra: Palabra que añadir a la batería de palabras, como máximo @n_palabras
@commands.command(name='add_word', help='El jugador añade una palabra')
async def add_word(ctx, palabra):
    PapeliGame.add_word(palabra)

    response = 'Palabra añadida  '  + palabra + ' por ' + ctx.message.author.name
    await ctx.send(response)

#@team: Nombre del equipo al que se quiere pertenecer, Null como predeterminado
@commands.command(name='join', help='Añade al jugador a la lista de jugadores con opción de indicar el equipo al que pertenece')
async def join(ctx, team = None):
    PapeliGame.add_player(ctx.message.author.name, team)
    
    if team != None:
        response =  'El jugador ' +  ctx.message.author.name + ' ha sido añadido al juego en el equipo ' + team +'.'
    else:
        response =  'El jugador ' +  ctx.message.author.name + ' ha sido añadido al juego.'

    await ctx.send(response)

@commands.command(name='start_game', help='Una vez que todos los jugadores hayan puesto las palabras se dará la opción de iniciar el juego')
async def start_game(ctx):

    PapeliGame.start_game()


@commands.command(name='ready', help='Inicia la ronda')
async def ready(ctx):
    
    await ctx.send()