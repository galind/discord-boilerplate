import logging
import discord
from logging import handlers
from discord.ext import commands
from . import config


logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
logging.getLogger('discord.http').setLevel(logging.ERROR)

handler = handlers.WatchedFileHandler(
    filename='discord.log',
    encoding='utf-8',
)

DT_FMT = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', DT_FMT, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

initial_extensions = ()


class Boilerplate(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='$',
            intents=discord.Intents.all()
        )


    async def setup_hook(self):
        for extension in initial_extensions:
            try:
                await self.load_extension(extension)
                print(f'Loaded: {extension}')
            except Exception as e:
                print(f'Not loaded: {extension} \n{e}')


    async def on_ready(self):
        print(f'Ready: {self.user}')


    async def start(self):
        return await super().start(
            config.APPLICATION_TOKEN,
            reconnect=True
        )
