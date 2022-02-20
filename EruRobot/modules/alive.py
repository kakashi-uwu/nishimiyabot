import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EruRobot.events import register
from EruRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/7bcbd82b7ea19702aaa75.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**hoi hoi [{event.sender.first_name} san](tg://user?id={event.sender.id}), I'm eru chitanda.** \n\n"
  TEXT += "∆ **I'm Working Properly** \n\n"
  TEXT += f"∆ **My hubby : [Baby](https://t.me/baby_hoii)** \n\n"
  TEXT += f"∆ **Library Version :** `{telever}` \n\n"
  TEXT += f"∆ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"∆ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**hope you're doing well!**"
  BUTTON = [[Button.url("Help", "https://t.me/eruxrobot?start=help"), Button.url("Support", "https://t.me/eruxsupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
