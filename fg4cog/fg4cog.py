import discord
from discord.ext import commands

class fg4cog:
    """Invites you to the support discord"""

    def __init__(self, bot):
        self.bot = bot
    #Support Discord invite
    @commands.command()
    async def supportinvite(self, ctx):
        """Invites you to the support discord"""

        await ctx.send("here you go: https://discord.gg/GET4DVk :smile:")
    #Start - Emojis
    @commands.command()
    async def smile(self, ctx):
        """sends a smile emoji."""

        await ctx.send(":smile:")
		
    @commands.command()
    async def frowns(self, ctx):
        """sends a frowning emoji."""

        await ctx.send(":frowning:")
		
    @commands.command()
    async def tongue(self, ctx):
        """sends a sticks out tongue emoji."""

        await ctx.send(":stuck_out_tongue:")
		
    @commands.command()
    async def thinking(self, ctx):
        """sends a thinking emoji."""

        await ctx.send(":thinking:")
	
    @commands.command()
    async def sob(self, ctx):
        """sends a sob emoji."""

        await ctx.send(":sob:")
		
    @commands.command()
    async def confused(self, ctx):
        """sends a confused emoji."""

        await ctx.send(":confused:")
		
    @commands.command()
    async def laughing(self, ctx):
        """sends a laughing emoji."""

        await ctx.send(":laughing:")
		
    @commands.command()
    async def rofl(self, ctx):
        """sends a rolling on the floor laughing emoji."""

        await ctx.send(":rofl:")
		
    @commands.command()
    async def thumbsup(self, ctx):
        """sends a thumb up emoji."""

        await ctx.send(":thumbsup:")
		
	@commands.command()
    async def thumbsdown(self, ctx):
        """sends a thumb down emoji."""

        await ctx.send(":thumbsdown:")	
	
	@commands.command()
    async def scream(self, ctx):
        """sends a scream emoji."""

        await ctx.send(":scream:")
		
	@commands.command()
    async def shootme(self, ctx):
        """sends a funny emoji combo."""

        await ctx.send("very well then. :frowning: :gun:")
		
	@commands.command()
    async def deadly(self, ctx):
        """sends a funny deadly emoji combo."""

        await ctx.send(":skull: :ghost: :alien:")
	
	#End - Emojis
	
	#Emoji Math - random text
	# TBD