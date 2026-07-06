import discord
from discord.ext import commands
from visual import draw_text_bracket

class MatchesModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bracket")
    async def view_bracket(self, ctx):
        t = self.bot.tournament
        bracket_view = draw_text_bracket(t)
        await ctx.send(f"```text\n{bracket_view}\n```")

    @commands.command(name="report")
    async def report_score(self, ctx, match_num: int, winner_name: str):
        t = self.bot.tournament
        if not t.started:
            return await ctx.send("The tournament hasn't started yet.")

        # Convert 1-based match index user types into 0-indexed code format
        match_idx = match_num - 1
        success = t.report_match(match_idx, winner_name)

        if success:
            await ctx.send(f"🏁 Match {match_num} updated! Winner set as {winner_name}.")
            
            # Check if that report triggered a whole new round transition
            current_round_matches = t.rounds[t.current_round]
            if len(current_round_matches) == 1 and current_round_matches[0]["winner"] is not None:
                await ctx.send(f"{current_round_matches[0]['winner']} has won the entire tournament!")
            else:
                await ctx.send("Updated Bracket Status:")
                await ctx.send(f"```text\n{draw_text_bracket(t)}\n```")
        else:
            await ctx.send("Invalid match number or player name. Please try again.")

async def setup(bot):
    await bot.add_cog(MatchesModule(bot))