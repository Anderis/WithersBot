import discord
import pytz
import os
import interactions
import asyncio
import sqlite3
import dice
import race
import base64
import leveling
from discord.ui import Button, View
from dotenv import load_dotenv
from discord.ext import commands
from race import get_race_info, get_movement_speed, get_racial_trait

load_dotenv()  # Load environment variables from .env file
TOKEN = os.getenv("DISCORD_TOKEN")  # Token grabber

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)  # Initialize commands.Bot with intents
bot.remove_command('help')

# ----- Write code between here -----

@bot.hybrid_command(name='help')
async def help_command(ctx):
    user_level = await get_user_level(ctx.author.id)
    await ctx.send(f"You are level {user_level}. Use `!info` to learn more about races.")
    
@bot.hybrid_command(name="info")
async def buttonmenu(ctx, race_name: str):
    if race_name is None:
        await ctx.send("Please provide a race. For example: `!info Human`")
        return

    print(f"Received race_name: {race_name}")  # debugging

    race_info = get_race_info(race_name)
    movement_speed = get_movement_speed(race_name)
    racial_trait = get_racial_trait(race_name)
    image_url = race_info.get('image_url', '')

    if race_info:
        print(f"Found race_info for {race_name}: {race_info}")  # debugging

        description = f"# **{race_info['title']}**\n\n"
        description += f"{race_info['description']}\n"
        
        if racial_trait:
            print(f"Found race movement: {movement_speed}")  # debugging
            print(f"Found racial trait: {racial_trait}")  # debugging
            description += f"## __RACIAL TRAIT__\n- Movement Speed: {movement_speed}{racial_trait}\n"

            embed = discord.Embed(
                title='',
                description=description,
                color=race_info['color']
            )
        
        if image_url:
            embed.set_thumbnail(url=image_url)

        await ctx.send(embed=embed)
    else:
        print(f"No race_info found for {race_name}")  # debugging

    
# ----- Write code between here -----

async def main():
    async with bot:
        await bot.start("")

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)

    if message.guild:
        channel = f"#{message.channel}"
        location = f"in {channel}"
    else:
        location = "in private DMs"

    await bot.process_commands(message)  # Process bot commands first

    await leveling.add_experience(message.author.id, 10)  # Adjust the amount as needed

    # Convert UTC time to EST timezone
    est_timezone = pytz.timezone('US/Eastern')
    utc_time = message.created_at.replace(tzinfo=pytz.UTC)
    est_time = utc_time.astimezone(est_timezone)

    timestamp = est_time.strftime("%Y-%m-%d %H:%M:%S")  # Format the timestamp

    if message.guild:
        print(f'{username} said: "{user_message}" in "{message.guild.name} #{message.channel.name}", at {timestamp}')
    else:
        print(f'{username} said: "{user_message}" in DMs at {timestamp}')


bot.run(TOKEN)