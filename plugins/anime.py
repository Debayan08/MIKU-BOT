from pyrogram import Client, types, filters
import requests

@Client.on_message(filters.command("anime"))
async def anime(client, message):
    user_name = message.from_user.username
    if len(message.command) < 2:
        return await message.reply_text(f"{user_name} Send **/anime AnimeName** to get info ℹ️.")
    message.command.pop(0)
    name = " ".join(message.command)
    res = requests.get(f"https://kitsu.io/api/edge//anime?filter[text]={name}")

    search_result = res.json()["data"]

    if len(search_result) < 1:
        return await message.reply_text("404 Anime not found")

    await message.reply_photo(
        photo=search_result[0]["attributes"]["posterImage"]["original"],
    )
    await message.reply(
        f"{user_name} \n **Title**:{search_result[0]['attributes']['titles']['en']}\n**Japanese**:{search_result[0]['attributes']['titles']['en_jp']}\n**PopularityRank**:{search_result[0]['attributes']['popularityRank']}\n**Age Rating**:{search_result[0]['attributes']['ageRatingGuide']}\n**Episode Count**:{search_result[0]['attributes']['episodeCount']}\n**Synopsis**:{search_result[0]['attributes']['synopsis']}",
    )
