"""Discord bot example. Adds some commands:
$hello    $hi
$date
Also, adds a clock as a background task.
Each N seconds it sends a message to a specified channel.
"""

import asyncio
from datetime import datetime

import discord

from config import DISCORD_API_TOKEN, DISCORD_CHANNEL_GENERAL
from tools.utils import utils
from tools.logger.logger import log
from tools.logger import logger

BACKGROUND_TASK_SLEEP_SEC = 60 * 15


class DiscordClient(discord.Client):

    async def setup_hook(self) -> None:
        # Create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.send_message_time())

    async def on_ready(self):
        log.info(f'Bot Logged in as {self.user}!')

    async def send_message_time(self):
        await self.wait_until_ready()
        channel = self.get_channel(int(utils.read_file_as_string(DISCORD_CHANNEL_GENERAL)))
        while not self.is_closed():
            await channel.send(f"Time: {datetime.now().strftime('%H:%M:%S')}")
            await asyncio.sleep(BACKGROUND_TASK_SLEEP_SEC)

    async def on_message(self, message):
        log.info(f'Message from {message.author}: {message.content}')

        if message.author == self.user:
            return

        if message.content.startswith('$hello') or message.content.startswith('$hi'):
            await message.channel.send(f"Hello {message.author.display_name}!")
        elif message.content.startswith('$date'):
            await message.channel.send(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def main():
    logger.add_stdout_handler()
    intents = discord.Intents.default()
    intents.message_content = True

    client = DiscordClient(intents=intents)
    api_token = utils.read_file_as_string(DISCORD_API_TOKEN)
    client.run(api_token)


if __name__ == '__main__':
    main()
