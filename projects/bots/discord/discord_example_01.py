"""Discord bot example. It requires the 'message_content' intent."""

import discord

from config import DISCORD_API_TOKEN
from tools.utils import utils
from tools.logger.logger import log
from tools.logger import logger


class DiscordClient(discord.Client):
    async def on_ready(self):
        log.info(f'Bot Logged in as {self.user}!')

    async def on_message(self, message):
        log.info(f'Message from {message.author}: {message.content}')

        if message.author == self.user:
            return

        if message.content.startswith('$hello') or message.content.startswith('$hi'):
            await message.channel.send(f"Hello {message.author.display_name}!")


def main():
    logger.add_stdout_handler()
    intents = discord.Intents.default()
    intents.message_content = True

    client = DiscordClient(intents=intents)
    api_token = utils.read_file_as_string(DISCORD_API_TOKEN)
    client.run(api_token)


if __name__ == '__main__':
    main()
