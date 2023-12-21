from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.types import CallbackQuery

  

event = {"-1152935968": "user", "event": "on"}


@Client.on_callback_query(filters.regex('event_(.*)'))
async def switch (client ,callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id 
    path ="/home/das/Downloads/bot-main/plugins/video.mp4"
    help_list = "🤖 MIKU-BOT Commands 💬\n- /anime - 🎌 Get anime details\n- /bored - 🕰️ Find activities to cure boredom \n- /jokes - 😄 Enjoy funny jokes\n- /rps - ✊✋✌️ Play Rock, Paper, Scissors\n- /waifu - ❤️ Find your waifu\n- /fact - 🧠 Discover interesting facts\n- /qr - 📱 Generate QR codes \n- /owner 🧑🏻‍💻- Contact of Owner"
    query_id_ = callback_query.id 
    input = callback_query.data.split("_", 1)[1]
    event_on = "EVENT ON 📢"
    event_off = "EVENT OFF 📢"
    if input == "on":
        event["channel_id"] = chat_id
        event["event"] = "on"
        await client.answer_callback_query(callback_query_id= query_id_,text=event_on, show_alert=True)
    elif input == "help":
        await client.send_video(chat_id,video = path, caption = help_list)
    else:
         event["channel_id"] = chat_id
         event["event"] = "off"
         await client.answer_callback_query(callback_query_id= query_id_,text=event_off, show_alert=True)


@Client.on_message(filters.command("event"))
async def eve (client, message):
    ms_g = 'Do you want to turn the event 🎐'
    keybord=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("OFF", callback_data="event_off")],
            [InlineKeyboardButton("ON", callback_data="event_on")]
        ])
    await message.reply(text = ms_g , reply_markup = keybord)

#https://docs.pyrogram.org/api/filters#module-pyrogram.filters

@Client.on_message(filters.new_chat_members)
async def new_member(client: Client, message: Message):
     user_name = message.from_user.username
     chat_titel = message.chat.title
     btn =InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Help-list", callback_data="event_help")]
    ])
     for member in message.new_chat_members:
      await message.reply(f'Welcome @{member.username} to {chat_titel} 🎉', reply_markup = btn)



     







