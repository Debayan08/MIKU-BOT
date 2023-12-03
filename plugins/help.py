from pyrogram import Client, filters


@Client.on_message(filters.command("help"))
async def help(client, message):
    user_name = message.from_user.username
    path ="/home/das/Downloads/bot-main/plugins/video.mp4"
    help_list =f"@{user_name}\n🤖 MIKU-BOT Commands 💬\n- /anime - 🎌 Get anime details\n- /bored - 🕰️ Find activities to cure boredom \n- /jokes - 😄 Enjoy funny jokes\n- /rps - ✊✋✌️ Play Rock, Paper, Scissors\n- /waifu - ❤️ Find your waifu\n- /fact - 🧠 Discover interesting facts\n- /qr - 📱 Generate QR codes \n - /owner 🧑🏻‍💻- Contact of Owner"
    await client.send_video(message.chat.id,video = path, caption = help_list)
    
