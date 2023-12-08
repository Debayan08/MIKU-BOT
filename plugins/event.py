from pyrogram import Client, filters ,types
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton
from pyrogram.types import CallbackQuery

event = {"channel_id": "user", "event": "off"}

@Client.on_callback_query()
async def switch (client ,callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id 
    query_id_ = callback_query.id 
    event_on = "EVENT ON 📢"
    event_off = "EVENT OFF 📢"

    if callback_query.data == "on":
       event["channel_id"] = chat_id
       event["event"] = "on"
       await client.answer_callback_query(callback_query_id= query_id_,text=event_on, show_alert=True)
    else:
        event["channel_id"] = chat_id
        event["event"] = "off"
        await client.answer_callback_query(callback_query_id= query_id_,text=event_off, show_alert=True)

@Client.on_message(filters.command("event"))
async def eve (client,message):
    ms_g = 'Do you want to turn the event 🎐'
    keybord=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("OFF", callback_data="off")],
            [InlineKeyboardButton("ON", callback_data="on")]
        ])
    await message.reply(text = ms_g , reply_markup = keybord)

@Client.on_chat_member_updated(filters.new_chat_members)
async def new_member(_, message):
    global event
    if event == True:
     new_m = message.from_user.username
     await message.reply(f'{new_m} Welcome to the group 🎐')
    else:
       return