# le epic bot by lll

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix="le*")

@bot.event
async def on_ready():
    print ("le epic has started playing games")
    print ("add me here " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="games"))

@bot.command(pass_context=True)
async def cmds(ctx):
    embed = discord.Embed(title="gamer commands", description="gamers go!11!11!11!11!1!", color=0x202913)
    embed.add_field(name="play", value="play the game")

@bot.command(pass_context=True)
async def play(ctx):
    await bot.say("play a game!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!11111!!!")

bot.run("NTM4ODQwMzcwMDY3NDA2ODQ5.Dy5rQg.igh4V9pcJLCPwZk-UG72BZYPL30")