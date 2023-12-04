from pyrogram import filters, types
from pyromod import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler


api_id = 28359218
api_hash = ''
token = ''
admin = 1

bot = Client('Bot', api_id=api_id, api_hash=api_hash, bot_token=token, plugins=dict(root='plugins', include=[
    'search', 'bored', 'help' ,'waifu','anime', 'jokes' ,'rps', 'qr.qr', 'fact', 'aki' , 'owner', 'captcha'
]))

      
@bot.on_message(filters.private & filters.user(admin) & filters.command('stat'))
async def stat(app: Client, msg: types.Message):
    await app.send_message(msg.chat.id, 'Working')
                                                                                            
bot.run()
