from pyrogram import Client, filters

@Client.on_message(filters.command("owner"))
async def owner(client, message):
    await message.reply_text("No.of 📞: +9832361550 \n 👤: @Das_2005_08")
