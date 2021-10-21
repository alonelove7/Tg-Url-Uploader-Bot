import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from script import Script
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup


@pyrogram.Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await update.reply_text(
        text=Script.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Script.START_BUTTONS
    )


@prrogram.Client.on_message(filters.command(["help"]) & filters.private)
async def help(bot, update):
    await update.reply_text(
        text=Script.HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=Script.HELP_BUTTONS
    )

@pyrogram.Client.on_message(filters.command(["about"]) & filters.private)
async def about(bot, update):
    await update.reply_text(
        text=Script.ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=Script.ABOUT_BUTTONS
    )

