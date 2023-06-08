from aiogram.dispatcher.filters.state import State,StatesGroup

class Kurslar(StatesGroup):
    idora = State()
    skill = State()
    phone = State()
    area = State()
    price = State()
    responsible = State()
    time = State()
    addition = State()
    finish = State()
