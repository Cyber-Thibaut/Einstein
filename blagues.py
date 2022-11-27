import discord
import os # default module
from dotenv import load_dotenv


load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "blague", description = "Renvoit une blague aléatoire")
async def blague(ctx):
    
    await ctx.send(f"{blague.joke}\n{blague.answer}")

bot.run(os.getenv('TOKEN'))

@bot.event
async def on_message_delete(message):
    await message.channel.respond(f"Le message de {message.author} a été supprimé 🚨🚨🚨")

@bot.event
async def on_message_edit(before, after):
    await before.channel.respond(f"{before.author} a édité son message 🚨🚨🚨")
