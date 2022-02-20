from pyrogram import Client as Bot
from pyrogram import idle
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN


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
