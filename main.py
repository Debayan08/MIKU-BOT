from pyrogram import filters, types
from pyromod import Client


api_id = 
api_hash = 
token = 
admin = 



bot = Client('Bot', api_id=api_id, api_hash=api_hash, bot_token=token, plugins=dict(root='plugins', include=[
  'bored', 'help' ,'waifu','anime', 'jokes' ,'rps', 'qr.qr', 'fact', 'owner','event','ytdl','chat_info'
]))

      
@bot.on_message(filters.private & filters.user(admin) & filters.command('stat'))
async def stat(app: Client, msg: types.Message):
    await app.send_message(msg.chat.id, 'Working')
                                                                                            
bot.run()
        
