from pyrogram import Client as Bot
from pyrogram import idle
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN
from asyncio import run
from loguru import logger
from pyrogram import Client, idle


async def main():
    bot_client = Client("bot")
    await bot_client.start()
    import helpers.bot
    setattr(helpers.bot, "bot_client", bot_client)
    bot_info = await bot_client.get_me()
    logger.success(f"Bot instance \"{bot_info.username}\" started.")
    await idle()
    logger.debug(f"Stopping bot instance \"{bot_info.username}\" ...")
    await bot_client.stop()
    logger.info(f"Bot instance \"{bot_info.username}\" stopped.")


if __name__ == '__main__':
    run(main())

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

bot.start()
run()
idle()
