from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
from pyrogram import Client,filters,ChatPermissions,enums
import random as R

audio_captcha = False
image_captcha = False
chat_p = False
audio = AudioCaptcha(voicedir='/path/to/voices')
image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])
cap = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
CAP_ANS = R.sample(cap,4)
data = audio.generate(cap)
audio.write( data , 'captcha.wav')

data = image.generate(cap)
image.write( data , 'captcha.png')

@Client.on_message(filters.command("captcha"))
async def captcha(client, message):
    await message.reply('🖼️ /img-captcha_on - Enable image CAPTCHA \n🚫🖼️ /img-captcha_off - Disable image CAPTCHA \n🔊 /aud-captcha_on - Enable audio CAPTCHA \n🚫🔊 /aud-captcha_off - Disable audio CAPTCHA')


@Client.on_message(filters.command("img-captcha_on"))
async def captcha(client, message):
    user = await message.chat.get_member(message.from_user.id)
    if user.status in (enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR):
      global image_captcha 
      image_captcha = True
      await message.reply_text('IMG-CAPTCHA activation engaged, within this crew. 🤖🔒')
    else:
       await message.reply_text('Admins only can do that !')

@Client.on_message(filters.command("img-captcha_off"))
async def captcha(client, message):
    user = await message.chat.get_member(message.from_user.id)
    if user.status in (enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR):
      global image_captcha 
      image_captcha = False
      await message.reply_text("IMG-CAPTCHA deactivation initiated, within this squad. 🚫🔓")
    else:
       await message.reply_text('Admins only can do that !')


@Client.on_message(filters.command("aud-captcha_on"))
async def captcha(client, message):
    user = await message.chat.get_member(message.from_user.id)
    if user.status in (enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR):
      global audio_captcha 
      audio_captcha = True
      await message.reply('AUD-CAPTCHA activation engaged, within this crew. 🤖🔒')
    else:
       await message.reply_text('Admins only can do that !')

@Client.on_message(filters.command("aud-captcha_off"))
async def captcha(client, message):
    user = await message.chat.get_member(message.from_user.id)
    if user.status in (enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR):
      global audio_captcha 
      audio_captcha = True
      await message.reply('AUD-CAPTCHA deactivation initiated, within this squad. 🚫🔓')
    else:
       await message.reply_text('Admins only can do that !')



@Client.on_message(filters.new_chat_members)
async def on_new_chat_members(Client, message):
    if image_captcha == True:
        await Client.restrict_chat_member(
            chat_id = message.chat.id,
            user_id = message.from_user.id,
            permissions= ChatPermissions(chat_p)
        )