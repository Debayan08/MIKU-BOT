from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton
from pyrogram.types import CallbackQuery
from pytube import YouTube
import os



@Client.on_message(filters.command("ytdl"))
async def anime(client, message):
    if len(message.command) < 2:
        user_name = message.from_user.username
        return await message.reply_text(f"@{user_name} Provide the youtube video link🔗 to download ")
    message.command.pop(0)
    keybord=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("YouTube-video", callback_data="YouTube_video")],
            [InlineKeyboardButton("YouTube-Audio", callback_data="YouTube_Audio")]
        ])
    await message.reply(text = "What you want to download:" , reply_markup = keybord)
    global link
    link = " ".join(message.command)


@Client.on_callback_query(filters.regex("YouTube_(.*)"))
async def switch(client, callback_query: CallbackQuery):
    global link
    if callback_query.data.split("_", 1)[1] == "video":
     youtubeObject = YouTube(link)
     youtubeObject = youtubeObject.streams.get_highest_resolution()
     try:
         youtubeObject.download()
     except:
         await client.send_message(callback_query.message.chat.id,"❌ An error has occurred")
     await client.send_message(callback_query.message.chat.id,f"Download is completed successfully✅")
     await client.send_video(callback_query.message.chat.id, video = f"{youtubeObject.title}.mp4", caption=f"Title: {youtubeObject.title}")
     os.remove(f"/home/das/Downloads/bot-main/{youtubeObject.title}.mp4")
    elif callback_query.data.split("_", 1)[1] == "Audio":
     try:
        video = YouTube(link)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=f"{video.title}.mp3")
        await client.send_message(callback_query.message.chat.id,f"Download is completed successfully✅")
     except KeyError:
       await client.send_message(callback_query.message.chat.id,"Unable to fetch video information. Please check the video URL or your network connection.")
     await client.send_audio(callback_query.message.chat.id,f"{video.title}.mp3", caption=f"Title: {video.title}")
     os.remove(f"/home/das/Downloads/bot-main/{video.title}.mp3")