import os
import discord
from discord.ext import commands
import custom_commands as cc

class PapeliBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        self.add_custom_commands()

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send('You do not have the correct role for this command.')

    def add_custom_commands(self):
        self.add_command(cc.nine_nine)
        self.add_command(cc.roll)
        self.add_command(cc.add_word)
        self.add_command(cc.create_game)
        self.add_command(cc.join)
        self.add_command(cc.start_game)
        self.add_command(cc.ready)
     