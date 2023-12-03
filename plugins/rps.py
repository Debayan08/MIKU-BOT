from pyrogram import Client, filters
import random

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
        user_id["points"] = 0
        user_id["user_id"] = 0
        bot_p["points"] = 0
        return True
    else:
        return False


@Client.on_message(filters.command("rps"))
async def rps(client, message):
    user_ID = message.from_user.id
    user_id["user_id"] = user_ID
    user_name = message.from_user.username
    y = user_id.get("user_id")
    u = check(user_ID)
    if u == True:
        await message.reply(
            f"👤 @{user_name}, you are officially registered 🗄 to join the game 🎮!\n Welcome aboard! 🌟 Get ready for an exciting adventure filled with fun and challenges! 🚀✨"
        )
        await message.reply(
            f"@{user_name} 👤 VS  @DasABAE_bot 🤖\nChoose your move: \n- /Rock 🪨\n- /Paper 📄\n- /Scissor ✂️\nLet the battle begin! Make your move wisely. "
        )
    else:
        await message.reply(f"@{user_name} \n {y} ``you are rejected``")


@Client.on_message(filters.command("Rock"))
async def rock(client, message):
    user_name = message.from_user.username
    user_ID = message.from_user.id
    check_id = check(user_ID)
    user_points = user_id.get("points")
    bot_points = bot_p.get("points")
    if check_id == True:
        choise = ["rock", "paper", "scissor"]
        bot = random.choice(choise)
        if "rock" == bot:
            await message.reply(
                f"@{user_name} Both players selected. It's a tie! \n choose between: \n ``/Rock 🪨, /Paper 📄, /Scissor ✂️"
            )
        elif bot == "scissor":
            await message.reply(
                f"@{user_name} Rock 🪨 smashes scissors ✂️ ! You win 🎉! \n choose between: \n ``/Rock 🪨, /Paper 📄, /Scissor ✂️"
            )
            await message.reply_text(f"👤: {user_points}")
            user_id["points"] += 1
            game_result = check_points(user_points, bot_points)
            if game_result == True:
                if user_points == 5:
                    await message.reply_text(
                        f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{user_name} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion"
                    )
                else:
                    await message.reply_text(
                        f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{user_name} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!"
                    )
        elif bot == "paper":
            await message.reply(
                f"@{user_name} Paper covers rock! You lose ☠️ \n choose between: \n ``/Rock 🪨, /Paper 📄, /Scissor ✂️"
            )
            await message.reply_text(f"🤖: {bot_points} ")
            bot_p["points"] += 1
            game_result = check_points(user_points, bot_points)
            if game_result == True:
                if user_points == 5:
                    await message.reply_text(
                        f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{user_name} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion"
                    )
                else:
                    await message.reply_text(
                        f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{user_name} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!"
                    )
    else:
        await message.reply(
            f"@{user_name} It is not your Game \n use /rps to PLAY this game 🎮"
        )


@Client.on_message(filters.command("Paper"))
async def Paper(client, message):
    user_name = message.from_user.username
    user_ID = message.from_user.id
    user_points = user_id.get("points")
    bot_points = bot_p.get("points")
    check_id = check(user_ID)
    if check_id == True:
        choise = ["rock", "paper", "scissor"]
        bot = random.choice(choise)
        if "paper" == bot:
            await message.reply(
                f"@{user_name} Both players selected. It's a tie! \n choose between: \n ``/Rock 🪨, /Paper 📄, /Scissor ✂️"
            )
        elif bot == "rock":
            await message.reply(
                f"@{user_name} Paper covers rock! You win 🎉! \n choose between: \n ``/Rock 🪨, /Paper 📄, /Scissor ✂️"
            )
            await message.reply_text(f"👤: {user_points}")
            user_id["points"] += 1
            game_result = check_points(user_points, bot_points)
            if game_result == True:
                if user_points == 5:
                    await message.reply_text(
                        f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{user_name} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion"
                    )
                else:
                    await message.reply_text(
                        f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{user_name} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!"
                    )
        elif bot == "scissor":
            await message.reply(
                f"@{user_name}Scissors cuts paper! You lose ☠️ \n choose between: \n ``/Rock 🪨, /Paper 📄, /Scissor ✂️"
            )
            await message.reply_text(f"🤖: {bot_points}")
            bot_p["points"] += 1
            game_result = check_points(user_points, bot_points)
            if game_result == True:
                if user_points == 5:
                    await message.reply_text(
                        f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{user_name} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion"
                    )
                else:
                    await message.reply_text(
                        f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{user_name} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!"
                    )
    else:
        await message.reply(
            f"@{user_name} It is not your Game \n use /rps to PLAY this game 🎮"
        )


@Client.on_message(filters.command("Scissor"))
async def Scissor(client, message):
    user_name = message.from_user.username
    user_ID = message.from_user.id
    user_points = user_id.get("points")
    bot_points = bot_p.get("points")
    check_id = check(user_ID)
    if check_id == True:
        choise = ["rock", "paper", "scissor"]
        bot = random.choice(choise)
        if "scissor" == bot:
            await message.reply(
                f"@{user_name} Both players selected. It's a tie! \n choose between: \n ``/Rock 🪨, /Paper 📄, /Scissor ✂️"
            )
        elif bot == "paper":
            await message.reply(
                f"@{user_name} Scissors cuts paper! You win 🎉! \n choose between: \n ``/Rock 🪨, /Paper 📄, /Scissor ✂️"
            )
            await message.reply_text(f"👤: {user_points}")
            user_id["points"] += 1
            game_result = check_points(user_points, bot_points)
            if game_result == True:
                if user_points == 5:
                    await message.reply_text(
                        f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{user_name} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion"
                    )
                else:
                    await message.reply_text(
                        f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{user_name} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!"
                    )
        elif bot == "rock":
            await message.reply(
                f"@{user_name} Rock smashes scissors! You lose ☠️ \n choose between: \n ``/Rock 🪨, /Paper 📄, /Scissor ✂️"
            )
            await message.reply_text(f"🤖: {bot_points}")
            bot_p["points"] += 1
            game_result = check_points(user_points, bot_points)
            if game_result == True:
                if user_points == 5:
                    await message.reply_text(
                        f"Victory in the epic Rock, Paper, Scissors showdown! 🏆 Check out the scoreboard:\n{user_name} - {user_points} 🌟\nBot - {bot_points} 💤\nMaster of the game, no one stands a chance against you! 🔥\n#RockPaperScissorsChampion"
                    )
                else:
                    await message.reply_text(
                        f"Unfortunately, you lost the Rock, Paper, Scissors match. Here are the scores:\n{user_name} - {user_points} \nBot - {bot_points} 🥺\n But hey, there's always another game waiting for a rematch!"
                    )
    else:
        await message.reply(
            f"@{user_name} It is not your Game \n use /rps to PLAY this game 🎮"
        )
