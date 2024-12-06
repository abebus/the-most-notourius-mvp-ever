import asyncio
import os
import aiohttp
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
import logging
import logging.config
import json

logging.basicConfig(level=logging.DEBUG)
# Bot token can be obtained via https://t.me/BotFather
TOKEN = os.getenv("TG_BOT_TOKEN")

# Initialize Bot instance
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# URLs for your resources
SCRAPY_URL = os.getenv("TG_SCRAPY_URL")
PREDICTOR_URL = os.getenv("TG_PREDICTOR_URL")


@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: Message):
    """Sends a welcome message."""
    await message.reply("Send me a link, and I'll process it for you!")


@dp.message()
async def process_link(message: Message):
    """Handles incoming messages with a link."""
    user_input = message.text.strip()

    # Validate if input is a URL
    if not user_input.startswith("http://") and not user_input.startswith("https://"):
        await message.reply("Please send a valid URL.")
        return

    async with aiohttp.ClientSession() as session:
        # Send the link to the first resource
        async with session.get(
            SCRAPY_URL, params={"url": user_input, "spider_name": "cian_spider"}
        ) as response1:
            response1.raise_for_status()
            data1 = await response1.json()
            logging.info(data1)

        # Use the response from the first resource to contact the second resource
        data = json.dumps(data1["items"][0], ensure_ascii=False)
        logging.info(data)
        async with session.post(
            PREDICTOR_URL, data=data, headers={"Content-Type": "application/json"}
        ) as response2:
            response2.raise_for_status()
            final_response = await response2.json()
            logging.info(final_response)

    # Send the final response back to the user
    await message.reply(
        text=(
            f"Предсказанная цена за кв. метр: {final_response["square_price"]}. "
            f"Полная: {float(final_response["square_price"]) * float(data1["items"][0]["area"])}. "
        )
    )


async def main() -> None:
    """Main function to start the bot."""
    # Start polling for updates
    await dp.start_polling(bot)


if __name__ == "__main__":
    import uvloop

    uvloop.install()

    asyncio.run(main())
