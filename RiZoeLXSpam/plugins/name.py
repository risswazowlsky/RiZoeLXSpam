import asyncio
import base64
import os
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, SUDO_USERS
from telethon import events

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)


@Riz.on(events.NewMessage(pattern=".setname"))
@Riz2.on(events.NewMessage(pattern=".setname"))
@Riz3.on(events.NewMessage(pattern=".setname"))
@Riz4.on(events.NewMessage(pattern=".setname"))
@Riz5.on(events.NewMessage(pattern=".setname"))
@Riz6.on(events.NewMessage(pattern=".setname"))
@Riz7.on(events.NewMessage(pattern=".setname"))
@Riz8.on(events.NewMessage(pattern=".setname"))
@Riz9.on(events.NewMessage(pattern=".setname"))
@Riz10.on(events.NewMessage(pattern=".setname"))
@Riz11.on(events.NewMessage(pattern=".setname"))
@Riz12.on(events.NewMessage(pattern=".setname"))
@Riz13.on(events.NewMessage(pattern=".setname"))
@Riz14.on(events.NewMessage(pattern=".setname"))
@Riz15.on(events.NewMessage(pattern=".setname"))
@Riz16.on(events.NewMessage(pattern=".setname"))
@Riz17.on(events.NewMessage(pattern=".setname"))
@Riz18.on(events.NewMessage(pattern=".setname"))
@Riz19.on(events.NewMessage(pattern=".setname"))
@Riz20.on(events.NewMessage(pattern=".setname"))
async def name(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = SET NAME\n\nCommand:\n\n.setname <Message to change name of spam ids>"
    if e.sender_id in SMEX_USERS:
        names = e.text.split(" ", 1)
        RiZoeL = names[1]
        if len(e.text) > 5:
            firstname = RiZoeL
            text = "Changing Name..."
            try:
                await e.client(functions.account.UpdateProfileRequest(first_name=firstname))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await event.edit("**Changed Name Successfully In** ✧ 𝗣𝗥∆𝗧𝗛𝗘𝗘𝗞 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧 ✧")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
