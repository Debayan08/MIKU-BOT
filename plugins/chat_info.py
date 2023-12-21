from pyrogram import Client, filters
from pyrogram.types import Message
import os

@Client.on_message(filters.new_chat_title )
async def new_member(client: Client, message: Message):
     chat_titel = message.chat.title
     await message.reply(f"🆕 chat title:\n{chat_titel} ")

@Client.on_message(filters.pinned_message )
async def new_member(client: Client, message: Message):
     chat_titel = message.chat.title
     chat = message.chat.pinned_message
     await message.reply(f"New pinned message:\n{chat} ")

@Client.on_message(filters.command("link"))
async def edit (client,message):
 chat = await client.get_chat(message.chat.id)
 await message.reply(chat.invite_link)

@Client.on_message(filters.command("chat_info"))
async def edit (client,message):
     chat = message.chat
     chat = await client.get_chat(chat.id)
     chat = await client.get_chat(chat.id)
     pinned_message = chat.pinned_message
     members_count = chat.members_count
     await client.download_media(chat.photo.big_file_id,file_name=f"{chat.title}.jpg")
     await client.send_photo(chat.id,f"/home/das/Downloads/bot-main/downloads/{chat.title}.jpg", caption=f"Chat-Titel: {chat.title}\nDescription: {chat.description}\nMembers: {members_count}\nPinned messages: {pinned_message.text}")
     os.remove(f"/home/das/Downloads/bot-main/downloads/{chat.title}.jpg")

@Client.on_message(filters.left_chat_member)
async def new_member(client: Client, message: Message):
     user_name = message.from_user.username
     chat_titel = message.chat.title
     await message.reply(f'@{message.left_chat_member.username} left the {chat_titel} 🥲')
