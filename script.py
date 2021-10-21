from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
<b>Hello {}!!!

I'am a url to telegram file or media uploader bot with permanent thumbnail support.</b>

<i>For More Details check Help 📜</i>
"""
    HELP_TEXT = """
<b>Link to Media or File</b>
- Send a link for upload to telegram file or media.

<b>Set Thumbnail</b>
- Send a photo to make it as permanent thumbnail.

<b>Deleting Thumbnail</b>
- Send /delthumb to deleting thumbnail.

<b>Show Thumbnail</b>
- Send /showthumb to view custom thumbnail.
"""
    ABOUT_TEXT = """
**Bot :** `URL Uploader`
**Creator :** [Vivek](https://telegram.me/vivektvp)
**Channel :** [Vk Projects](https://telegram.me/VKPROJECTS)
**Credits :** `Everyone in this journey`
**Language :** [Python3](https://python.org)
**Library :** [Pyrogram v1.2.0](https://pyrogram.org)
**Server :** [Heroku](https://heroku.com)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤔 Help', callback_data='help'),
        InlineKeyboardButton('🤖 About', callback_data='about'),
        ],[
        InlineKeyboardButton('Close🔐', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 About', callback_data='about'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠 Home', callback_data='home'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    )
