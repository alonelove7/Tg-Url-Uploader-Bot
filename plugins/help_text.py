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
from translation import Translation
from helper_funcs.forcesub import ForceSub
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup


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
from translation import Translation
from helper_funcs.forcesub import ForceSub
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup


@pyrogram.Client.on_message(pyrogram.filters.private & filters.incoming & filters.command("help"))
async def _help(bot, msg):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
        await bot.send_message(
             msg.chat.id,
             "**Here's How to Use Me **\n" + Data.HELP,
             reply_markup=InlineKeyboardMarkup(Data.home_buttons)
         )

@pyrogram.Client.on_message(pyrogram.filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
        user = await bot.get_me()
	   mention = user["mention"]
	      await bot.send_message(
		  msg.chat.id,
		    Data.START.format(msg.from_user.mention, mention),
		       reply_markup=InlineKeyboardMarkup(Data.buttons)
	 )

@pyrogram.Client.on_message(pyrogram.filters.private & filters.incoming & filters.command("about"))
async def about(bot, msg):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
        await bot.send_message(
          msg.chat.id,
            Data.ABOUT,
             disable_web_page_preview=True,
               reply_markup=InlineKeyboardMarkup(Data.home_buttons),
         )
