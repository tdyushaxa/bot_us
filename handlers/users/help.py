from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.talim_state import Ustoz_state

@dp.message_handler(CommandHelp(),state=Ustoz_state.all_states)
async def bot_help(message: types.Message,state:FSMContext):
    await state.reset_state()
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
