from pyrogram import Client, types, filters
import requests

@Client.on_message(filters.command("bored"))
async def bored(client, message):
    user_name = message.from_user.username
    response = requests.get("https://www.boredapi.com/api/activity/")
    data = response.json()["activity"]

    await message.reply(f" {user_name} Activity 🏃: {data}")