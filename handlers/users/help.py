from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp
from states.talim_state import Ustoz_state, Shogir_kerak, Sherik_kerak, Xodim_kerak, Ish_joyi


@dp.message_handler(CommandHelp(),state=Ustoz_state.all_states)
async def bot_help(message: types.Message,state:FSMContext):
    await state.finish()
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))


@dp.message_handler(commands='help', state=Shogir_kerak.all_states)
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))


@dp.message_handler(commands='help', state=Sherik_kerak.all_states)
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))


@dp.message_handler(commands='help', state=Xodim_kerak.all_states)
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))


@dp.message_handler(commands='help', state=Ish_joyi.all_states)
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message, state: FSMContext):
    await state.reset_state()
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))

