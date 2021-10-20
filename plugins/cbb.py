#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b><i>📛 Builder : @cyber_punk_me\n📛 Channel 1 : <a href='t.me/Cinemaglitz/7'>CinemaGlitz</a>\n📛 Channel 2 : <a href='t.me/CineGramamOfficial/2'>CinemaGramam</a>\n📛 Group 1 : <a href='https://t.me/joinchat/SDCy7kWHxS_kouZn'>CineGlitz</a>\n📛 Group 2 :<a href='https://t.me/joinchat/WGzYiotIH4QwZjRl'>CineGramam</a></b></i>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass