from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, SUDO_USERS
from telethon import events
import os
import random
import sys

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

@Riz.on(events.NewMessage(pattern=".restart"))
@Riz2.on(events.NewMessage(pattern=".restart"))
@Riz3.on(events.NewMessage(pattern=".restart"))
@Riz4.on(events.NewMessage(pattern=".restart"))
@Riz5.on(events.NewMessage(pattern=".restart"))
@Riz6.on(events.NewMessage(pattern=".restart"))
@Riz7.on(events.NewMessage(pattern=".restart"))
@Riz8.on(events.NewMessage(pattern=".restart"))
@Riz9.on(events.NewMessage(pattern=".restart"))
@Riz10.on(events.NewMessage(pattern=".restart"))
@Riz11.on(events.NewMessage(pattern=".restart"))
@Riz12.on(events.NewMessage(pattern=".restart"))
@Riz13.on(events.NewMessage(pattern=".restart"))
@Riz14.on(events.NewMessage(pattern=".restart"))
@Riz15.on(events.NewMessage(pattern=".restart"))
@Riz16.on(events.NewMessage(pattern=".restart"))
@Riz17.on(events.NewMessage(pattern=".restart"))
@Riz18.on(events.NewMessage(pattern=".restart"))
@Riz19.on(events.NewMessage(pattern=".restart"))
@Riz20.on(events.NewMessage(pattern=".restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "**Restarting Your** 𝗣𝗥𝗔𝗧𝗛𝗘𝗘𝗞 𝗦𝗣∆𝗠𝗕𝗢𝗧.. Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Riz.disconnect()
        except Exception:
            pass
        try:
            await Riz2.disconnect()
        except Exception:
            pass
        try:
            await Riz3.disconnect()
        except Exception:
            pass
        try:
            await Riz4.disconnect()
        except Exception:
            pass
        try:
            await Riz5.disconnect()
        except Exception:
            pass
        try:
            await Riz6.disconnect()
        except Exception:
            pass
        try:
            await Riz7.disconnect()
        except Exception:
            pass
        try:
            await Riz8.disconnect()
        except Exception:
            pass
        try:
            await Riz9.disconnect()
        except Exception:
            pass
        try:
            await Riz10.disconnect()
        except Exception:
            pass
        try:
            await Riz11.disconnect()
        except Exception:
            pass
        try:
            await Riz12.disconnect()
        except Exception:
            pass
        try:
            await Riz13.disconnect()
        except Exception:
            pass
        try:
            await Riz14.disconnect()
        except Exception:
            pass
        try:
            await Riz15.disconnect()
        except Exception:
            pass
        try:
            await Riz16.disconnect()
        except Exception:
            pass
        try:
            await Riz17.disconnect()
        except Exception:
            pass
        try:
            await Riz18.disconnect()
        except Exception:
            pass
        try:
            await Riz19.disconnect()
        except Exception:
            pass
        try:
            await Riz20.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
