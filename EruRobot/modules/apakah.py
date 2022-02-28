import random
from EruRobot.events import register
from EruRobot import telethn

APAKAH_STRING = ["chala ja bsdk", 
                 "No idea", 
                 "Sasta hai", 
                 "India hai, chalta hai", 
                 "Arey you Pointing me out", 
                 "That's nonsense",
                 "Impossible",
                 "Okay go on",
                 "Ask me somthing else",
                 "Really ?",
                 "baby-kun is my boyfriend,god, owner and love"
                 ]


@register(pattern="^/what ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('gimme some questions')
        return
    await event.reply(random.choice(APAKAH_STRING))

__help__ = """
➢ `/what`*:* <argument> you'll get some random.....or maybe annoying answers"""
__mod_name__ = "❣️Wʜᴀᴛ❣️"
