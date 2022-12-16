import asyncio
from core.bot import Bot


async def run_bot():
    bot = Bot()
    await bot.start()


def main():
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
