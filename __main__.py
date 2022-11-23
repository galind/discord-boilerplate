import asyncio
from core.bot import Boilerplate


async def run_bot():
    bot = Boilerplate()
    await bot.start()


def main():
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
