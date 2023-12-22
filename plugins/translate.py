from pyrogram import Client, filters
from translate import Translator
   
@Client.on_message(filters.command("t"))
async def edit (client,message):
 user_name = message.from_user.username
 message.command.pop(0)
 if len(message.command) < 2:
  await message.reply_text(f"@{user_name} Pls enter something for translation\n /t <laguage> <your sentence or word>")
 else:
  try :
   lang = message.command[0]
   translator = Translator(to_lang=f"{lang}") 
   message.command.pop(0)
   sentence =" ".join(message.command)
   translation = translator.translate(sentence)
   await message.reply_text(f"Sentence: {sentence}\nTranslation: {translation}")
  except Exception as e:
   await message.reply(e)
 