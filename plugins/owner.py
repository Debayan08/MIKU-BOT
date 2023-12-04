from pyrogram import Client, filters

@Client.on_message(filters.command("owner"))
async def owner(client, message):
    await message.reply_text("🌟 Owner Details 🌟\nName: @Das_2005_08 \nAge: 18 🎂  \nGitHub: https://github.com/Debayan08 🐙  \nLanguage: Python 🐍  \nEmail: debayanabae2005@gmail.com 📧  \nInstagram 📸: das_abae\n The mind is everything. What you think, you become. - Mahabharata🌌✨")
