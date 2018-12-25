import discord
from discord.ext import commands

class fg4cog0001:
    """Invites you to the support discord"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self):
        """Invites you to the support discord"""

        await self.bot.say("here you go: https://discord.gg/dNWRmKg :smile:")
		
    @commands.command()
    async def smile(self):
        """smiles for you."""

        await self.bot.say(":smile:")
