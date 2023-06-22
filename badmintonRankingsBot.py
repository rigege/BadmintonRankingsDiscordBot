import discord
import botFunctions

TOKEN = "" # <--- insert your application token here
GUILD = "" # <--- insert your guild/server name here

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for server in client.guilds:
        if server.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{server.name}(id: {server.id})'
    )

class Buttons(discord.ui.View):         # inherited button class that presents usable buttons to the use and adds fucntioanlity when an object is created
    
    def __init__(self, msg):            # a message is passed to the class so the program knows which message the buttons are to edit
        super().__init__()
        self.message = msg
    
    @discord.ui.button(emoji="⬅")
    async def prevBut(self, interaction: discord.Interaction, button: discord.ui.button):
        await interaction.response.defer()      # response is deferred so discord won't raise an error since discord expects an interaction response when button is pressed
        self.message = await self.message.edit(embed=botFunctions.getAdj("page_prev", self.message.embeds[0]))
        
    @discord.ui.button(emoji="➡")
    async def nextBut(self, interaction: discord.Interaction, button: discord.ui.button):
        await interaction.response.defer()
        self.message = await self.message.edit(embed=botFunctions.getAdj("page_next", self.message.embeds[0]))
        
@client.event
async def on_message(message):
    if message.author == client.user:      # checks if the message is sent by the bot itself, in which case nothing is sent to prevent unwanted bot recursion
        return
    if ("rank.ms" in message.content.lower()):
        URL = "https://bwf.tournamentsoftware.com/ranking/category.aspx?rid=70&category=472"
        
        to_print = botFunctions.singlesRank(URL, "Men's Singles")           # getting the embed to send to the guild text channel
        
        msg = await message.channel.send(embed=to_print)
        buts = Buttons(msg)
        await message.channel.send(view=buts)           # sending the buttons to be displayed for the user
        
    if ("rank.md" in message.content.lower()):
        URL = "https://bwf.tournamentsoftware.com/ranking/category.aspx?rid=70&category=474"
        
        to_print = botFunctions.doublesRank(URL, "Men's Doubles")
        
        msg = await message.channel.send(embed=to_print)
        buts = Buttons(msg)
        await message.channel.send(view=buts)
        
    if ("rank.ws" in message.content.lower()):
        URL = "https://bwf.tournamentsoftware.com/ranking/category.aspx?rid=70&category=473"
        
        to_print = botFunctions.singlesRank(URL, "Women's Singles")
        
        msg = await message.channel.send(embed=to_print)
        buts = Buttons(msg)
        await message.channel.send(view=buts)
        
    if ("rank.wd" in message.content.lower()):
        URL = "https://bwf.tournamentsoftware.com/ranking/category.aspx?rid=70&category=475"
        
        to_print = botFunctions.doublesRank(URL, "Women's Doubles")
        
        msg = await message.channel.send(embed=to_print)
        buts = Buttons(msg)
        await message.channel.send(view=buts)
        
    if ("rank.xd" in message.content.lower()):
        URL = "https://bwf.tournamentsoftware.com/ranking/category.aspx?rid=70&category=476"
        
        to_print = botFunctions.doublesRank(URL, "Mixed Doubles")
        
        msg = await message.channel.send(embed=to_print)
        buts = Buttons(msg)
        await message.channel.send(view=buts)
    if ("rank.help" in message.content.lower()):
        info = "Men's Singles```rank.ms```Women's Singles```rank.ws```Men's Doubles```rank.md```Women's Doubles```rank.wd```Mixed Doubles```rank.xd```\n\
            Use the ⬅ and ➡ arrows under the rankings to change pages."
        to_print = discord.Embed(title="Bot Help", description=info, colour=discord.Colour.from_str("#80DEEA"))
        await message.channel.send(embed=to_print)

client.run(TOKEN)