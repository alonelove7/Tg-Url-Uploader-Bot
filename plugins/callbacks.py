import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from plugins.yt_dlp_button import yt_dlp_call_back
from plugins.dl_button import ddl_call_back
from translation import Translation
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_callback_query()
async def button(bot, update):
    if "|" in update.data:
        await yt_dlp_call_back(bot, update)
    elif "=" in update.data:
        await ddl_call_back(bot, update)
    elif update.data == "home":
        await update.message.edit_text(
            text=Script.START_TEXT.format(update.from_user.mention),
            reply_markup=Script.START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=Script.HELP_TEXT,
            reply_markup=Script.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=Script.ABOUT_TEXT,
            reply_markup=Script.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()
