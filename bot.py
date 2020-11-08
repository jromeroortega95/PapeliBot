# bot.py
import os
from papelibot import PapeliBot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = PapeliBot(command_prefix='!')
bot.run(TOKEN)
