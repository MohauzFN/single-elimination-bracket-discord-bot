import discord
from discord.ext import commands

class RegistrationModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join")
    async def join_tournament(self, ctx):
        t = self.bot.tournament
        if not t.active:
            return await ctx.send("No tournament is currently open for registration.")
        if t.started:
            return await ctx.send("Too late! The tournament has already started.")
        
        success = t.add_player(ctx.author.name)
        if success:
            await ctx.send(f"{ctx.author.mention} has registered! Total players: {len(t.players)}")
        else:
            await ctx.send("You are already registered.")

    @commands.command(name="leave")
    async def leave_tournament(self, ctx):
        t = self.bot.tournament
        if t.started:
            return await ctx.send("You cannot leave an active tournament.")
        
        success = t.remove_player(ctx.author.name)
        if success:
            await ctx.send(f"{ctx.author.name} has left the tournament.")
        else:
            await ctx.send("You aren't registered in this tournament.")

async def setup(bot):
    await bot.add_cog(RegistrationModule(bot))