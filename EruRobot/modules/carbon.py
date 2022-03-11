from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from EruRobot import pbot
from EruRobot.utils.errors import capture_err
from EruRobot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


MEMEK = "https://telegra.ph/file/8408e4ef091c3d97c8cb9.jpg"

@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=MEMEK,
        caption=f""" **ʜᴏɪ ᴋɪᴅᴅᴏ I'ᴍ ᴇʀᴜ ᴄʜɪᴛᴀɴᴅᴀ  **  

**Oᴡɴᴇʀ ʀᴇᴘᴏ : [ᴄʜᴇʀʀʏ-ᴋᴜɴ](https://t.me/baby_hoii)**
╔════════════════════╗
┣× ʀᴇᴘᴏ ɪs ᴘʀɪᴠᴀᴛᴇ
┣× ᴏᴡɴᴇʀ ɪs ʜᴀʀᴀᴍɪ 
┣× ʏᴏᴜ ᴄᴀɴ'ᴛ ɢᴇᴛ ɪᴛ 
┣× sᴏ ᴋɪɴᴅʟʏ ғᴜᴄᴋ ᴏғғ
╚════════════════════╝

**Gʀᴏᴡ ᴜᴘ ᴋɪᴅ, ᴛʜᴇɴ I'ʟʟ ᴛʜɪɴᴋ ᴀʙᴏᴜᴛ ɪᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "GɪᴛHᴜʙ", url="https://github.com/baby-kun"),
                    InlineKeyboardButton(
                        "Cʜᴇʀʀʏ-ᴋᴜɴ", url="https:/t.me/yoi_babes"), 
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ", url="https://t.me/eruXsupport")
                ]
            ]
        )
    )

