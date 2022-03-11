import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EruRobot.events import register
from EruRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/1f55761762cf30a02cb22.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Kᴏɴ'ɴɪᴄʜɪᴡᴀ [{event.sender.first_name} san](tg://user?id={event.sender.id}), I'ᴍ ᴇʀᴜ.** \n\n"
  TEXT += "**╔═══──────═══╗** \n\n"
  TEXT += f"┣[× Cʜᴇʀʀʏ-ᴋᴜɴ : [Cʜᴇʀʀʏ-ᴋᴜɴ](https://t.me/baby_hoii)** \n\n"
  TEXT += f"┣[× **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"┣[× **Tᴇʟᴇᴛʜᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"┣[× **ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**╚═══──────═══╝"
  BUTTON = [[Button.url("Hᴇʟᴘ", "https://t.me/eruxrobot?start=help"), Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/eruxsupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
