from pyrogram import Client, filters
import asyncio
from akinator import (
    CantGoBackAnyFurther,
    InvalidAnswer,
    AsyncAkinator,
    Answer,
    Theme,
)


@Client.on_message(filters.command("aki"))
async def test(client, message):
 aki = AsyncAkinator()
 q = await aki.start_game()
 await message.reply(f"{q}")
 answer = message.command[0]
 while aki.progression <= 80:
    if answer == 'back':
            # go back a question if response is "back"
        try:
             await aki.back()
             await message.reply_text ('went back 1 question')
        except CantGoBackAnyFurther:
                await message.reply_text('cannot go back any further!')
        else:
            try:
                answer = Answer.from_str(answer)
            except InvalidAnswer:
                await message.reply_text ('Invalid answer')
            else:
                await aki.answer(answer)
        
        await message.reply_text (f'{aki.question}: ')
        answer = message.command[0]


    first_guess = await aki.win()

    if first_guess:
        # await message.reply out its first guess's details
        await message.reply('name:', first_guess.name)
        await message.reply('desc:', first_guess.description)
        await message.reply_photo('image:', first_guess.absolute_picture_path)