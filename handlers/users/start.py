from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboards import menu
from loader import dp,db
from states.talim_state import Ustoz_state, Shogir_kerak, Sherik_kerak, Xodim_kerak, Ish_joyi

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    id = message.from_user.id
    fullname = message.from_user.full_name
    try:
        db.add_user(id=id,name=fullname)
    except:
        pass

    await message.answer(f"Salom, {message.from_user.full_name}! yo'nalishni tanlang", reply_markup=menu)


@dp.message_handler(commands='start', state=Ustoz_state.all_states)
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(f"Salom, {message.from_user.full_name}! yo'nalishni tanlang", reply_markup=menu)


@dp.message_handler(commands='start', state=Shogir_kerak.all_states)
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(f"Salom, {message.from_user.full_name}! yo'nalishni tanlang", reply_markup=menu)


@dp.message_handler(commands='start', state=Sherik_kerak.all_states)
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(f"Salom, {message.from_user.full_name}! yo'nalishni tanlang", reply_markup=menu)


@dp.message_handler(commands='start', state=Xodim_kerak.all_states)
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(f"Salom, {message.from_user.full_name}! yo'nalishni tanlang", reply_markup=menu)


@dp.message_handler(commands='start', state=Ish_joyi.all_states)
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(f"Salom, {message.from_user.full_name}! yo'nalishni tanlang", reply_markup=menu)



