import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

async def main() -> None:
    # Bot token can be obtained via https://t.me/BotFather
    TOKEN = os.getenv("TG_BOT_TOKEN")

    dp = Dispatcher()

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    import uvloop
    uvloop.install()

    asyncio.run(main())