from pyrogram import Client, types, filters, enums
import requests

@Client.on_message(filters.command("jokes"))
async def d_jokes(client, message):
    data = requests.get(
        "https://v2.jokeapi.dev/joke/Pun?blacklistFlags=nsfw,religious,political"
    )
    setup = data.json()["setup"]
    delivery = data.json()["delivery"]

    await message.reply(f"{setup}\n{delivery}")
    