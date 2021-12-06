from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else ""
  

          
rizoel = "✧ [𝗥𝗔𝗙𝗘𝗡-𝗕𝗢𝗧] 𝗶𝘀 𝗔𝗹𝗶𝘃𝗲 ✧͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏͏\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"

    
rizoel += f"┣➣ **Groups ᴍᴇ** : [Tap](https://t.me/CariKenalanBebas)\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

rizoel += f"😁[𝙸 𝙻𝙾𝚅𝙴 𝙼𝚈 𝙲𝚁𝚄𝚂𝙷](https://t.me/Rafens)"            
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SMEX_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
