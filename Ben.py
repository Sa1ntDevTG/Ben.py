from telethon import events
import requests
from uniborg.util import admin_cmd
import random as rd 

@borg.on(admin_cmd("ben2"))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    num = rd.randint(1, 4)
    if num == 1:
        m = "Ben talking: Yes."
    if num == 2:
        m = "Ben talking: No."
    if num == 3:
    	m = "Ben talking: Ho-ho-ho!"
    if num == 4:
    	m = "Ben talking: Ew-ew-ew ..."
    await borg.send_message(
        event.chat_id,
        m,
        reply_to=message_id
    )
    await event.delete()
    #Бэн, когда?
@borg.on(admin_cmd("benwhen"))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    num = rd.randint(1, 10)
    age = rd.randint(25, 120)
    if num == 1:
        m = "Ben talking: across 20min."
    if num == 2:
        m = "Ben talking: across week."
    if num == 3:
    	m = "Ben talking: tomorrow."
    if num == 4:
    	m = "Ben talking: never..."
    if num == 5:
    	m = "Ben talking:Not sure, ask me later."
    if num == 6:
    	m = "Ben talking: Coming soon."
    if num == 7:
    	m = "Ben talking: repeat soon."
    if num == 8:
    	m = "Ben talking: across month"
    if num == 9:
    	m = "Ben talking: Yesterday."
    if num == 10:
        m = "Ben talking: When you get knocked up " + str(rd.randint(25, 120))
    await borg.send_message(
        event.chat_id,
        m,
        reply_to=message_id
    )
    await event.delete()
