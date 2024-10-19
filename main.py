import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define intents
intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.message_content = True

# Bot setup
bot = commands.Bot(command_prefix='!', intents=intents)

# Get channel name
channelName = os.getenv('CHANNEL_NAME')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_voice_state_update(member, before, after):
    try:
        print(f'Voice state update detected for member: {member.name}')
        print(f'Before channel: {before.channel}, After channel: {after.channel}')
        
        # User joins a voice channel
        if before.channel is None and after.channel is not None:
            print(f'{member.name} has joined {after.channel.name}')
            text_channel = discord.utils.get(member.guild.text_channels, name=channelName)
            if text_channel:
                print(f'Sending join message to text channel: {text_channel.name}')
                await text_channel.send(f'{member.display_name} has joined the voice channel {after.channel.name}')

        # User leaves a voice channel
        elif before.channel is not None and after.channel is None:
            print(f'{member.name} has left {before.channel.name}')
            text_channel = discord.utils.get(member.guild.text_channels, name=channelName)
            if text_channel:
                print(f'Sending leave message to text channel: {text_channel.name}')
                await text_channel.send(f'{member.display_name} has left the voice channel {before.channel.name}')

        # User switches voice channels
        elif before.channel is not None and after.channel is not None and before.channel != after.channel:
            print(f'{member.name} has moved from {before.channel.name} to {after.channel.name}')
            text_channel = discord.utils.get(member.guild.text_channels, name=channelName)
            if text_channel:
                print(f'Sending move message to text channel: {text_channel.name}')
                await text_channel.send(f'{member.display_name} has moved from {before.channel.name} to {after.channel.name}')
    except Exception as e:
        print(f'Error processing voice state update: {e}')

# Run the bot
print('Starting bot...')
token = os.getenv('DISCORD_TOKEN')
if token is None:
    print("DISCORD_TOKEN not found. Please set the environment variable.")
else:
    print("DISCORD_TOKEN found.")
try:
    bot.run(token)
except Exception as e:
    print(f'Error starting bot: {e}')
