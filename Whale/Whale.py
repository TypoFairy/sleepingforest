import discord
from discord.ext import commands
from random import choice as rndchoice
from .utils.dataIO import fileIO
from .utils import checks
import os

defaults = [
    "Twentysix's Floppy Disk",
    "Eslyium's Hentai Collection",
    "A Nuke",
    "A Loaf Of Bread",
    "My Hand",
    "Will's SquidBot",
    "JennJenn's Penguin Army",
    "Red's Transistor",
    "Asu\u10e6's Wrath",
    "Skordy's Keyboard"]

class Whale:
    """Whale command."""

    def __init__(self, bot):
        self.bot = bot
        self.items = fileIO("data/whale/items.json", "load")

    def save_items(self):
        fileIO("data/whale/items.json", 'save', self.items)

    @commands.group(pass_context=True, invoke_without_command=True)
    async def whale(self, ctx, *, user : discord.Member=None):
        """Whale a user"""
        if ctx.invoked_subcommand is None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("I'm not a whale! I'm a Moo! **Chomp** " + user.name)
                return
            await self.bot.say("-The Filthy Whale " + user.name + " is spotted in their natural habitat " +
                               (rndchoice(self.items) + "-"))

    @whale.command()
    async def add(self, item):
        """Adds an item *Use Quotations marks to add a sentence*"""
        if item in self.items:
          await self.bot.say("That habitat has already been entered")
        else:
          self.items.append(item)
          self.save_items()
          await self.bot.say("Habitat added.")

    @whale.command()
    @checks.is_owner()
    async def remove(self, item):
        """Removes item"""
        if item not in self.items:
          await self.bot.say("This doesnt exist Moo!")
        else:
            self.items.remove(item)
            self.save_items()
            await self.bot.say("habitat removed.")

def check_folders():
    if not os.path.exists("data/whale"):
        print("Creating data/whale folder...")
        os.makedirs("data/whale")

def check_files():
    f = "data/whale/items.json"
    if not fileIO(f, "check"):
        print("Creating empty items.json...")
        fileIO(f, "save", defaults)

def setup(bot):
    check_folders()
    check_files()
    n = Whale(bot)
    bot.add_cog(n)
