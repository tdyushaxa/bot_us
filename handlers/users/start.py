from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menuKeyboards import menu
from loader import dp
from states.talim_state import Ustoz_state


@dp.message_handler(commands='start',state=Ustoz_state.all_states)
async def bot_start(message: types.Message,state:FSMContext):
    await state.reset_state()
    await message.answer(f"Salom, {message.from_user.full_name}! yo'nalishni tanlang",reply_markup=menu)



@dp.message_handler(commands='start')
async def bot_start(message: types.Message,state:FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}! yo'nalishni tanlang",reply_markup=menu)

