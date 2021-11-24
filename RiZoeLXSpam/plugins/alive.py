from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"
  

          
rizoel = "✧ 𝗣𝗥∆𝗧𝗛𝗘𝗘𝗞 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧 𝗜𝗦 𝗔𝗟𝗜𝗩𝗘 ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **𝗣𝗥𝗔𝗧𝗛𝗘𝗘𝗞 𝗦𝗣∆𝗠𝗕𝗢𝗧 ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"
    
rizoel += f"┣➣ **ᴀʙᴏᴜᴛ ᴍᴇ** : [JOIN](https://t.me/aboutpratheek)\n"

rizoel += f"┣➣ **ᴄʀᴇᴀᴛᴏʀ** : [JOIN](https://t.me/pratheek06)\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

rizoel += f"🖤 [𝐎𝐖𝐍𝐄𝐑-𝐗𝐃](https://t.me/pratheek06) 🖤"            
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SMEX_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
