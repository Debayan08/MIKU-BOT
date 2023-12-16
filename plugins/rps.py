from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton
from pyrogram.types import CallbackQuery
from pyrogram import Client, filters
import random
import asyncio
import time


user_id = {"user_id": "user", "points": 1}
bot_p = {"points": 1}


def check(USER_ID):
    User = user_id.get("user_id")
    if User == USER_ID:
        return True
    else:
        return False
    
def check_points(user_points, bot_points):
    if user_points == 5 or bot_points == 5:
        asyncio.sleep(3)
        user_id["points"] = 0
        user_id["user_id"] = 0
        bot_p["points"] = 0
        return True
    else:
        return False
    


@Client.on_callback_query(filters.regex('rps_(.*)'))
async def switch (client ,callback_query: CallbackQuery):
    choise = ["rock", "paper", "scissor"]
    bot = random.choice(choise) 
    username  = callback_query.from_user.mention
    user_points = user_id.get("points")
    bot_points = bot_p.get("points")
    check_id = check(callback_query.from_user.id)
    query_id_ = callback_query.id 
    game_result = check_points(user_points, bot_points)
    keybord=InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Rock 🪨 ", callback_data="rps_rock")],[InlineKeyboardButton("Paper 📄" , callback_data="rps_paper")],[InlineKeyboardButton("scissors ✂️" , callback_data="rps_scissors")]
    ])
    await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id,text = callback_query.data.split("_", 1)[1])
    if check_id == True:
      if callback_query.data.split("_", 1)[1]== bot:
           await asyncio.sleep(1)
           await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Both players selected {username}. It's a tie!",reply_markup = keybord)
      elif callback_query.data.split("_", 1)[1]== "rock":
          if bot == "scissors":
              user_id["points"] += 1
              await asyncio.sleep(1)
              await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id,text=f"Rock 🪨 smashes scissors ✂️ ! You win 🎉!\n points:\n{username} :{user_points}\n🤖 : {bot_points - 1}",reply_markup = keybord)
              if game_result == True:
                if user_points == 5:
                     await asyncio.sleep(1)
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{username} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion")
                elif bot_points == 5:
                     await asyncio.sleep(1)
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{username} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!")
          else:
              bot_p["points"] += 1
              await asyncio.sleep(1)
              await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Paper covers rock! You lose \npoints:\n{username} :{user_points-1} \n 🤖 : {bot_points}",reply_markup = keybord)
              if game_result == True:
                if user_points == 5:
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{username} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion")
                elif bot_points == 5:
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{username} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!")
              
      elif callback_query.data.split("_", 1)[1]== "paper":
          if bot == "rock":
              user_id["points"] += 1
              await asyncio.sleep(1) 
              await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text =f"Paper covers rock! You win 🎉\npoints:\n{username} :{user_points} \n 🤖 : {bot_points - 1}",reply_markup = keybord)    
              if game_result == True:
                if user_points == 5:
                     await asyncio.sleep(1)
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{username} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion")
                elif bot_points == 5:
                     await asyncio.sleep(1)
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{username} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!")
          else:
              await asyncio.sleep(1)
              bot_p["points"] += 1
              await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text =f"Scissors cuts paper! You lose ☠️ \npoints:\n{username} :{user_points - 1} \n 🤖 : {bot_points}",reply_markup = keybord)
              if game_result == True:
                await asyncio.sleep(1)
                if user_points == 5:
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{username} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion")
                elif bot_points == 5:
                     await asyncio.sleep(1)
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{username} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!")
      elif callback_query.data.split("_", 1)[1]== "scissors":
          if bot == "paper":
              user_id["points"] += 1
              await asyncio.sleep(1)
              await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text =f"Scissors cuts paper! You win 🎉! \npoints:\n{username} :{user_points} \n 🤖 : {bot_points - 1}",reply_markup = keybord)
              if game_result == True:
                if user_points == 5:
                     await asyncio.sleep(1)
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{username} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion")
                elif bot_points == 5:
                     await asyncio.sleep(1)
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{username} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!")
          else:
              bot_p["points"] += 1
              await asyncio.sleep(1)
              await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text =f"Rock smashes scissors! You lose ☠️ \npoints:\n{username} :{user_points - 1} \n 🤖 : {bot_points}",reply_markup = keybord)
              if game_result == True:
                if user_points == 5:
                     await asyncio.sleep(1)
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{username} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion")
                elif bot_points == 5:
                     await asyncio.sleep(1)
                     await client.edit_message_text(chat_id= callback_query.message.chat.id,message_id = callback_query.message.id, text = f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{username} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!")
    else:
         await asyncio.sleep(1)
         await client.answer_callback_query(callback_query_id= query_id_,text="This is not your game!🎮\n Use /rps to play!", show_alert=True)
     

@Client.on_message(filters.command("rps"))
async def rps(client, message):
    user_ID = message.from_user.id
    user_id["user_id"] = user_ID
    user_name = message.from_user.username
    u = check(user_ID)
    keybord=InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Rock 🪨 ", callback_data="rps_rock")],[InlineKeyboardButton("Paper 📄" , callback_data="rps_paper")],[InlineKeyboardButton("scissors ✂️" , callback_data="rps_scissors")]
    ])
    if u == True:
        reply = await message.reply_text(
            f"👤 @{user_name}, you are officially registered 🗄 to join the game 🎮! \nLet the battle begin! Make your move wisely. 🚀✨",reply_markup = keybord
        )
        global new_message_id
        new_message_id = reply.id
    else:
        return 




    
