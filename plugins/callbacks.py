from script import Script
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    mention = user["mention"]
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.message_id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Script.START_TEXT.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Script.buttons),
            )
    elif query == "about":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Script.ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Script.home_buttons),
        )
    elif query == "help":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="**Here's How to use me**\n" + Data.HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Script.home_buttons),
        )
