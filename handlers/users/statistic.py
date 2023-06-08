from aiogram import types


from loader import dp, db, bot


@dp.message_handler(commands='statistika')
async def bot_help(message: types.Message):
    admin = 1091980088
    user_count = db.count_users()[0]
    await bot.send_message(admin,user_count)