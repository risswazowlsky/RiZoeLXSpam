from .. import Riz, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)
    
HELP_PIC = "https://telegra.ph/file/4003d1db7e5354152cd29.jpg"

RiZoeLX = "🔥 𝗣𝗥𝗔𝗧𝗛𝗘𝗘𝗞 𝗦𝗣∆𝗠𝗕𝗢𝗧 🔥\n\n"
 
RiZoeLX += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ♡︎𝗣𝗥𝗔𝗧𝗛𝗘𝗘𝗞 𝗦𝗣∆𝗠𝗕𝗢𝗧♡︎__\n\n"

RiZoeLX += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

RiZoeLX += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n `.setname` - to change Name\n .`inviteall` - to add members using spam bots\n .`restart` - to restart all spam bots\n\n"
 
RiZoeLX += f" ↧ 𝙹𝙾𝙸𝙽/𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳𝚂 ↧\n\n"

RiZoeLX += f" `.join` - to join public channel/groups\n `.pjoin` - to join public channel/groups\n `.leave` - to leave public/private channel/groups\n\n"
 
RiZoeLX += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

RiZoeLX += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.delayspam` - this cmd use for delay spam"
 
RiZoeLX += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.delayspam` - this cmd use for delay spam\n\n"

RiZoeLX += f"© @Pratheek06 | @AboutPratheek\n"


@Riz.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SMEX_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=RiZoeLX)                                                         
