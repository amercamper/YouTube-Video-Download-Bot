import asyncio
from pyrogram import Client, enums
from Youtube.config import Config
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def handle_force_subscribe(bot, message):
    try:
        invite_link = await bot.create_chat_invite_link(int(Config.CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return 400
    except Exception as e:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Failed to create invite link. Please try again later.",
            disable_web_page_preview=True,
        )
        return 400

    try:
        user = await bot.get_chat_member(int(Config.CHANNEL), message.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=message.from_user.id,
                text="Sorry Sir, You are Banned. Contact My Support Group.",
                disable_web_page_preview=True,
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=("Please join my updates channel to use me!\n\n"
                  "Due to overload, only channel subscribers can use me!"),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Please Join My Channel 🤖", url=invite_link.invite_link)
                    ],
                ]
            ),
        )
        return 400
    except Exception as e:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Something went wrong. Contact My Support Group.",
            disable_web_page_preview=True,
        )
        return 400

    return 200  # Assuming this is a success code
