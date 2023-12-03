from pyrogram import Client,filters
import requests

@Client.on_message(filters.command("waifu"))
async def waifu(client, message):
    user_name = message.from_user.username
    response = requests.get(
        "https://api.waifu.im/search?included_tags=waifu&height=>=2000"
    )
    data = response.json()["images"][0]
    await message.reply_text(user_name)
    await message.reply_photo(
        photo=data["url"], caption=data["tags"][0]["description"]
    )