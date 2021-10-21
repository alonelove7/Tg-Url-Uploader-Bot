from pyrogram.types import InlineKeyboardButton


class Script:
    # Start Message
    START_TEXT = """
Hey {}

I am Fastest Url Uploader Bot. 
Just send me the Url to get Started !

Made With 💕 By @Tellybots_4u
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏡 Return Home", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("📡 Update Channel", url="https://t.me/tellybots_4u")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("👲 About", callback_data="about")
        ],
        [InlineKeyboardButton("🚦 Bot Status", url="https://t.me/tellybots_4u")],
        [InlineKeyboardButton("💬 Support Group", url="https://t.me/tellybots_support")],
    ]

    # Help Message
    HELP_TEXT = """
Just send me the media and you will get the link!

 **Available Commands** 

/about - About The Bot
/help - This Message
/start - Start the Bot
    """

    # About Message
    ABOUT_TEXT = """
**About This Bot** 

A telegram Fastest Url Uploader Bot 

Source Code : [Click Here](https://t.me/tellybots_digital)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Tellybots_4u
    """
