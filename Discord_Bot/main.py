from typing import Final
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents, Client, Message
from responses import get_response

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
bot: commands.Bot = commands.Bot(command_prefix='%', intents=intents)
# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# STEP 5: COMMAND TO COLLECT DATA
@bot.command(name='collectdata')
async def collectdata(ctx: commands.Context) -> None:
    response = f"CPU Usage: {cpu_usage}%\n" \
               f"Memory Total: {memory.total} bytes\n" \
               f"Memory Used: {memory.used} bytes\n" \
               f"Disk Total: {disk.total} bytes\n" \
               f"Disk Used: {disk.used} bytes\n" \
               f"Network Bytes Sent: {network.bytes_sent} bytes\n" \
               f"Network Bytes Received: {network.bytes_recv} bytes"

    await ctx.send(response)

# STEP 6: MAIN ENTRY POINT
def main() -> None:
    bot.run(token=TOKEN)


if __name__ == '__main__':
    main()
