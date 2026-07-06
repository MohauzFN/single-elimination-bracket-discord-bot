import discord
from discord.ext import commands
from visual import draw_text_bracket

class AdminModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="t_create")
    @commands.has_permissions(administrator=True)
    async def create_tournament(self, ctx):
        t = self.bot.tournament
        t.__init__() # Reset everything
        t.active = True
        await ctx.send("A new tournament registration has been opened! Type `!join` to enter.")

    @commands.command(name="t_start")
    @commands.has_permissions(administrator=True)
    async def start_tournament(self, ctx):
        t = self.bot.tournament
        if not t.active:
            return await ctx.send("Create a tournament first using `!t_create`.")
        if len(t.players) < 2:
            return await ctx.send("You need at least 2 players to start a tournament.")
        
        t.generate_bracket()
        await ctx.send("The brackets have been shuffled and locked! Round 1 begins now.")
        bracket_view = draw_text_bracket(t)
        await ctx.send(f"```text\n{bracket_view}\n```")

async def setup(bot):
    await bot.add_cog(AdminModule(bot))