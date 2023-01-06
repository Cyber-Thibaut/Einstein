import discord
import os # default module
from dotenv import load_dotenv
from blagues_api import BlaguesAPI, BlagueType


load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "blague", description = "Renvoit une blague aléatoire")
async def blague(ctx):
    
    await ctx.send(f"{blague.joke}\n{blague.answer}")

blagues = BlaguesAPI(os.getenv('TOKENBLAGUE'))
class blague(discord.ui.View):
    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Quel niveau d'alerte ?", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Global",
                description="Chef c'est calme ce soir !"
            ),
            discord.SelectOption(
                label="Dev",
                description="Vive le Python !"
            ),
            discord.SelectOption(
                label="Dark",
                description="Ca va être tout noir ! *TA GUEULE!*"
            ),
            discord.SelectOption(
                label="Limite",
                description="Ouh Pinaise !"
            ),
            discord.SelectOption(
                label="Beauf",
                description="Sortez couvert !"
            ),
            discord.SelectOption(
                label="Blonde",
                description="Sortez couvert !"
            )
        ]
    )
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        if select.values[0]=="Global":
            blague = await blagues.random_categorized(BlagueType.GLOBAL)
            embed = discord.Embed(title = blague.type)
            embed.add_field(name=blague.joke,value=f"||{blague.answer}||")
            await interaction.response.send_message(embed=embed)
        if select.values[0]=="Dev":
            blague = await blagues.random_categorized(BlagueType.DEV)
            embed = discord.Embed(title = blague.type)
            embed.add_field(name=blague.joke,value=f"||{blague.answer}||")
            await interaction.response.send_message(embed=embed)
        if select.values[0]=="Dark":
            blague = await blagues.random_categorized(BlagueType.DARK)
            embed = discord.Embed(title = blague.type)
            embed.add_field(name=blague.joke,value=f"||{blague.answer}||")
            await interaction.response.send_message(embed=embed)
        if select.values[0]=="Limite":
            blague = await blagues.random_categorized(BlagueType.LIMIT)
            embed = discord.Embed(title = blague.type)
            embed.add_field(name=blague.joke,value=f"||{blague.answer}||")
            await interaction.response.send_message(embed=embed)
        if select.values[0]=="Beauf":
            blague = await blagues.random_categorized(BlagueType.BEAUF)
            embed = discord.Embed(title = blague.type)
            embed.add_field(name=blague.joke,value=f"||{blague.answer}||")
            await interaction.response.send_message(embed=embed)
        if select.values[0]=="Blonde":
            blague = await blagues.random_categorized(BlagueType.BLONDE)
            embed = discord.Embed(title = blague.type)
            embed.add_field(name=blague.joke,value=f"||{blague.answer}||")
            await interaction.response.send_message(embed=embed)
@bot.slash_command(name="blagues", description = "Envoie une blague")
async def flavor(ctx):
    await ctx.respond("Quel niveau de blague ?", view=blague(), ephemeral=True, delete_after=3)

@bot.event
async def on_message_delete(message):
    await message.channel.respond(f"Le message de {message.author} a été supprimé 🚨🚨🚨")

@bot.event
async def on_message_edit(before, after):
    await before.channel.respond(f"{before.author} a édité son message 🚨🚨🚨")
bot.run(os.getenv('TOKEN'))