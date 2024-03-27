from pyrogram import enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from pyrogram import filters
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.database import Database
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
import logging

logger = logging.getLogger(__name__)
db = Database(Var.DATABASE_URL, Var.name)

if MY_PASS:
    buttonz = ReplyKeyboardMarkup(
        [
            ["start⚡️", "help📚", "DC"],
            ["ping📡", "status📊"]
        ],
        resize_keyboard=True
    )
else:
    buttonz = ReplyKeyboardMarkup(
        [
            ["start⚡️", "help📚", "DC"],
            ["ping📡", "status📊"]
        ],
        resize_keyboard=True
    )


@StreamBot.on_message((filters.command("start") | filters.regex('start⚡️')) & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined:** \n\n__My New Friend__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await b.send_message(chat_id=m.chat.id, text="You Are Banned\n\n  He will help you", disable_web_page_preview=True)
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/57bb7cd0a8566bd93f3df.jpg",
                caption="<i>Join CHANNEL TO USE ME🔐</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join now 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
            )
            return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>Use Our V2 Bot</i> <b> <a href='https://t.me/Direct_D_L_Bot'>FILE TO LINK BOT </a></b>",
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo="https://graph.org/file/6f07d643cbcfa5b3ccffb.jpg",
        caption=f'Hi {m.from_user.mention(style="md")}!,\nI am Telegram File to Link Generator Bot with Channel support.\nSend me any file and get a direct download link and streamable link.!',
        reply_markup=buttonz
    )


@StreamBot.on_message((filters.command("help") | filters.regex('help📚')) & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined **\n\n__My New Friend__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await b.send_message(chat_id=m.chat.id, text="You Are Banned\n\n  He will help you", disable_web_page_preview=True)
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://graph.org/file/6f07d643cbcfa5b3ccffb.jpg",
                Caption="**JOIN SUPPORT GROUP TO USE this Bot!**\n\n__Due to Overload, Only Channel Subscribers can use the Bot!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Use Our V2 Bot__ [FILE TO LINK](https://t.me/Direct_D_L_Bot).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b> Send me any file or video i will give you streamable link and download link.</b>\n
<b> I also support Channels, add me to you Channel and send any media files and see miracle✨ also send /list to know all commands""",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Channel", url="https://t.me/Linux_Bots")],
                [InlineKeyboardButton("Developer", url="https://t.me/Prime_Alok")]
            ]
        )
    )
