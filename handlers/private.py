
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**sᴀʏᴀ ᴋᴀɢᴜʀᴀ ᴍᴜsɪᴄ ʙᴏᴛ ʏᴀɴɢ ᴅɪ ᴅᴇsᴀɪɴ ᴋʜᴜsᴜs ᴜɴᴛᴜᴋ ᴍᴇᴍᴜᴛᴀʀ ʟᴀɢᴜ ᴅɪ ᴠᴄɢ ʏᴀʜ ᴛᴏᴅ
ᴊɪᴋᴀ ᴀᴅᴀ ᴋᴇɴᴅᴀʟᴀ ʜᴜʙᴜɴɢɪ ᴍᴀsᴛᴇʀ sᴀʏᴀ : [ᴋᴇɴᴢʜᴜ](https://t.me/TripleNineee))**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔺 ᴏᴡɴᴇʀ 🔺", url="https://t.me/TripleNineee")
                  ],[
                    InlineKeyboardButton(
                        "🔺 ᴄʜᴀɴɴᴇʟ 🔺", url="https://t.me/inibotsaya"
                    ),
                    InlineKeyboardButton(
                        "🔺 ɢʀᴏᴜᴘ 🔺", url="https://t.me/Kenzusupport"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🔺 ᴘᴇʀɪɴᴛᴀʜ 🔺", url="https://telegra.ph/file/4aab5b0c3035e6d54fb99.jpg"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("kagura") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Saya Siap memutar lagu kesukaanmu tod**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔺 ɢʀᴏᴜᴘ 🔺", url="https://t.me/Kenzusupport")
                ]
            ]
        )
   )
