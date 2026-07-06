import os
import asyncio
import discord
from discord.ext import commands
from tournament import Tournament

# ================= CONFIGURE SERVER =================
# Replace this with your actual Discord Server (Guild) ID, Not entered for security reasons
SERVER_ID = 67  
# =================================================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.tournament = Tournament()

MODULES = ["module_admin", "module_registration", "module_matches"]

# Global check: This stops the bot from running ANY command if it's not in the pre-configured server
@bot.check
async def check_server(ctx):
    if ctx.guild is None:
        await ctx.send("Tournament commands cannot be used in Direct Messages.")
        return False
    if ctx.guild.id != SERVER_ID:
        # Silently ignore or alert if someone tries to use it in another server
        return False
    return True

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print(f"Pre-configured Server ID locked to: {SERVER_ID}")
    print("------")

async def main():
    async with bot:
        for module in MODULES:
            await bot.load_extension(module)
        
        # Replace 'YOUR_TOKEN_HERE' with your actual bot token, Not entered for security reasons
        await bot.start("67")

if __name__ == "__main__":
    asyncio.run(main())
