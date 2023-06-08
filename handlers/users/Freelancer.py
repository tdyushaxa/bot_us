import re
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.menuKeyboards import agree
from keyboards.inline.callbackData import  freelencer
from keyboards.inline.inline_keyboard import frelencer
from loader import dp, bot
import time as wait_time
from states.frelenser_state import Ustoz_state, Ish_joyi, Sherik_kerak, Shogir_kerak, Xodim_kerak

phone_number = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
admin = 1091980088


@dp.message_handler(Text(equals='Freelancer'), state=Ustoz_state.all_states)
async def setEduction(msg: types.Message):
    await msg.answer('tanlang', reply_markup=frelencer)


@dp.message_handler(Text(equals='Freelancer'))
async def setEduction(msg: types.Message):
    await msg.answer('tanlang', reply_markup=frelencer)


@dp.callback_query_handler(freelencer.filter(item__name="ustoz"))
async def get_talim_state(call: types.CallbackQuery):
    await call.message.answer(
        f"""
Ustoz topish uchun ariza berish
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
        """, reply_markup=ReplyKeyboardRemove()
    )
    await call.answer(cache_time=60)
    await call.message.answer('ism va familayangizni kriiting')
    await Ustoz_state.fullname.set()


@dp.message_handler(state=Ustoz_state.fullname)
async def get_fullname(msg: types.Message, state: FSMContext):
    fullname = msg.text
    if len(fullname) >= 5:
        await state.update_data({
            'fullname': fullname
        })
        await msg.answer('Yoshingizni kiriting')
        await Ustoz_state.next()
    else:
        await msg.answer('ismingiz va familayingiz 5 ta harfdan ko\'p bo\'lishi lozim ')
        await Ustoz_state.fullname.set()
        await msg.answer('ism va familayangizni kriiting')


@dp.message_handler(state=Ustoz_state.age)
async def get_age(msg: types.Message, state: FSMContext):
    age = msg.text
    if age.isnumeric():
        await state.update_data({
            'age': age
        })

        await msg.answer(
            """
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Python, Java, GO
            """
        )
        await Ustoz_state.next()
    else:
        await msg.answer('siz harf kiritdingiz')
        await Ustoz_state.age.set()
        await msg.answer('yoshingizni kiriting')


@dp.message_handler(state=Ustoz_state.skill)
async def get_skill(msg: types.Message, state: FSMContext):
    skill = msg.text.title().split(',')
    await state.update_data({
        'skill': skill

    })
    await msg.answer("""
📞 Telefon: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67

    """)
    await Ustoz_state.next()


@dp.message_handler(state=Ustoz_state.phone)
async def get_phone(msg: types.Message, state: FSMContext):
    if re.match(phone_number, msg.text):
        phone = msg.text
        await state.update_data({
            'phone': phone
        })
        await msg.answer('''
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.

        ''')
        await Ustoz_state.next()

    else:
        await msg.answer('siz no\'tog\'ri shaklda kiritdingiz yoki harf kriitidingiz')
        await state.finish()
        await Ustoz_state.phone.set()
        await msg.answer("""
📞 Telefon: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67

            """)


@dp.message_handler(state=Ustoz_state.area)
async def get_hudud(msg: types.Message, state: FSMContext):
    area = msg.text
    await state.update_data({
        'area': area
    })
    await msg.answer('''
    💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
    ''')
    await Ustoz_state.next()


@dp.message_handler(state=Ustoz_state.price)
async def get_price(msg: types.Message, state: FSMContext):
    price = msg.text

    await state.update_data({
        'price': price
    })
    await msg.answer('''
        👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
        ''')
    await Ustoz_state.next()


@dp.message_handler(state=Ustoz_state.job)
async def get_job(msg: types.Message, state: FSMContext):
    job = msg.text
    await state.update_data({
        'job': job
    })
    await msg.answer('''
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
    ''')
    await Ustoz_state.next()


@dp.message_handler(state=Ustoz_state.time)
async def get_time(msg: types.Message, state: FSMContext):
    time = msg.text
    await state.update_data({
        'time': time
    })
    await msg.answer('''
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
    ''')
    await Ustoz_state.next()


@dp.message_handler(state=Ustoz_state.goal)
async def get_goal(msg: types.Message, state: FSMContext):
    goal = msg.text
    await state.update_data({
        'goal': goal
    })
    data = await state.get_data()
    fullname = data.get('fullname')
    age = data.get('age')
    skills = data.get('skill')
    hashtag = ''
    for x in skills:
        hashtag += x.replace(x, ' #' + x)
    skill = ','.join(skills)
    phone = data.get('phone')
    area = data.get('area')
    price = data.get('price')
    job = data.get('job')
    time = data.get('time')
    goal = data.get('goal')
    username = msg.from_user.username
    message = f'''
    Ustoz kerak:
🎓 Shogird: {fullname}
🌐 Yosh: {age}
📚 Texnologiya: {skill}
🇺🇿 Telegram: @{username}
📞 Aloqa: {phone} 
🌐 Hudud: {area} 
💰 Narxi: {price} 
👨🏻‍💻 Kasbi: {job} 
🕰 Murojaat qilish vaqti: {time}
🔎 Maqsad: {goal}
#shogird  {hashtag} #{area}
    '''
    wait_time.sleep(2)
    await msg.answer(message)
    await msg.answer("malumotlaringizni to'g'riligiga ishonch hosil qiling! ", reply_markup=agree)
    await Ustoz_state.next()


@dp.message_handler(state=Ustoz_state.finish)
async def set_finish(msg: types.Message, state: FSMContext):
    text = msg.text
    if text == 'Ha':
        data = await state.get_data()
        fullname = data.get('fullname')
        age = data.get('age')
        skills = data.get('skill')
        hashtag = ''
        for x in skills:
            hashtag += x.replace(x, ' #' + x)
        skill = ','.join(skills)
        phone = data.get('phone')
        area = data.get('area')
        price = data.get('price')
        job = data.get('job')
        time = data.get('time')
        goal = data.get('goal')
        username = msg.from_user.username
        message = f'''
        Ustoz kerak:
🎓 Shogird: {fullname}
🌐 Yosh: {age}
📚 Texnologiya: {skill}
🇺🇿 Telegram: @{username}
📞 Aloqa: {phone} 
🌐 Hudud: {area} 
💰 Narxi: {price} 
‍💻 Kasbi: {job} 
🕰 Murojaat qilish vaqti: {time}
🔎 Maqsad: {goal}
#shogird {hashtag} #{area}
            '''
        wait_time.sleep(1)
        await bot.send_message(admin, message)
        await msg.answer('maumotlaringi adminga yuborildi 12-24 soat oralag\'ida kanalda e\'lon qilinadi',
                         reply_markup=ReplyKeyboardRemove())
        await state.finish()
    else:
        await state.finish()
        await msg.answer('malumotlaringiz qabul qilinmadi', reply_markup=ReplyKeyboardRemove())
        await msg.answer('Tanlang', reply_markup=frelencer)


@dp.callback_query_handler(freelencer.filter(item__name="job"))
async def get_talim_state(call: types.CallbackQuery):
    await call.message.answer(
        f"""
ISh joyi topish uchun ariza berish
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
        """, reply_markup=ReplyKeyboardRemove()
    )
    await call.answer(cache_time=60)
    await call.message.answer('ism va familayangizni kriiting', reply_markup=ReplyKeyboardRemove())
    await Ish_joyi.fullname.set()


@dp.message_handler(state=Ish_joyi.fullname)
async def ish_get_fullname(msg: types.Message, state: FSMContext):
    fullname = msg.text
    if len(fullname) >= 4:
        await state.update_data({
            'fullname': fullname
        })
        await msg.answer('Yoshingizni kiriting')
        await Ish_joyi.next()
    else:
        await msg.answer('ismingiz va familayingiz 5 ta harfdan ko\'p bo\'lishi lozim ')
        await Ish_joyi.fullname.set()
        await msg.answer('ism va familayangizni kriiting')


@dp.message_handler(state=Ish_joyi.age)
async def get_age(msg: types.Message, state: FSMContext):
    age = msg.text
    if age.isnumeric():
        await state.update_data({
            'age': age
        })

        await msg.answer(
            """
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Python, Java, GO
            """
        )
        await Ish_joyi.next()
    else:
        await msg.answer('siz harf kiritdingiz')
        await Ish_joyi.age.set()
        await msg.answer('yoshingizni kiriting')


@dp.message_handler(state=Ish_joyi.skill)
async def ish_get_skill(msg: types.Message, state: FSMContext):
    skill = msg.text.title().split(',')
    await state.update_data({
        'skill': skill

    })
    await msg.answer("""
📞 Telefon: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67

    """)
    await Ish_joyi.next()


@dp.message_handler(state=Ish_joyi.phone)
async def ish_get_phone(msg: types.Message, state: FSMContext):
    if re.match(phone_number, msg.text):
        phone = msg.text
        await state.update_data({
            'phone': phone
        })
        await msg.answer('''
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.

        ''')
        await Ish_joyi.next()

    else:
        await msg.answer('siz no\'tog\'ri shaklda kiritdingiz yoki harf kriitidingiz')
        await state.finish()
        await Ish_joyi.phone.set()
        await msg.answer("""
📞 Telefon: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67

            """)


@dp.message_handler(state=Ish_joyi.area)
async def ish_get_hudud(msg: types.Message, state: FSMContext):
    area = msg.text
    await state.update_data({
        'area': area
    })
    await msg.answer('''
    💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
    ''')
    await Ish_joyi.next()


@dp.message_handler(state=Ish_joyi.price)
async def ish_get_price(msg: types.Message, state: FSMContext):
    price = msg.text

    await state.update_data({
        'price': price
    })
    await msg.answer('''
        👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
        ''')
    await Ish_joyi.next()


@dp.message_handler(state=Ish_joyi.job)
async def ish_get_job(msg: types.Message, state: FSMContext):
    job = msg.text
    await state.update_data({
        'job': job
    })
    await msg.answer('''
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
    ''')
    await Ish_joyi.next()


@dp.message_handler(state=Ish_joyi.time)
async def ish_get_time(msg: types.Message, state: FSMContext):
    time = msg.text
    await state.update_data({
        'time': time
    })
    await msg.answer('''
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
    ''')
    await Ish_joyi.next()


@dp.message_handler(state=Ish_joyi.goal)
async def ish_get_goal(msg: types.Message, state: FSMContext):
    goal = msg.text
    await state.update_data({
        'goal': goal
    })
    data = await state.get_data()
    fullname = data.get('fullname')
    age = data.get('age')
    skills = data.get('skill')
    skill = ','.join(skills)
    hashtag = ''
    for x in skills:
        hashtag += x.replace(x, ' #' + x)
    phone = data.get('phone')
    area = data.get('area')
    price = data.get('price')
    job = data.get('job')
    time = data.get('time')
    goal = data.get('goal')
    username = msg.from_user.username

    message = f'''
    Ish joyi kerak::

👨‍💼 Xodim: {fullname}
🌐 Yosh: {age}
📚 Texnologiya: {skill}
🇺🇿 Telegram: @{username}
📞 Aloqa: {phone} 
🌐 Hudud: {area} 
💰 Narxi: {price} 
👨🏻‍💻 Kasbi: {job} 
🕰 Murojaat qilish vaqti: {time}
🔎 Maqsad: {goal}
#xodim {hashtag} #{area}
    '''
    wait_time.sleep(1)
    await msg.answer(message)
    await msg.answer("malumotlaringizni to'g'riligiga ishonch hosil qiling! ", reply_markup=agree)
    await Ish_joyi.next()


@dp.message_handler(state=Ish_joyi.finish)
async def set_ish_finish(msg: types.Message, state: FSMContext):
    text = msg.text
    if text == 'Ha':
        data = await state.get_data()
        fullname = data.get('fullname')
        age = data.get('age')
        skills = data.get('skill')
        skill = ','.join(skills)
        hashtag = ''
        for x in skills:
            hashtag += x.replace(x, ' #' + x)
        phone = data.get('phone')
        area = data.get('area')
        price = data.get('price')
        job = data.get('job')
        time = data.get('time')
        goal = data.get('goal')
        username = msg.from_user.username

        message = f'''
    Ish joyi kerak::

‍💼 Xodim: {fullname}
🌐 Yosh: {age}
📚 Texnologiya: {skill}
Telegram: @{username}
📞 Aloqa: {phone} 
🌐 Hudud: {area} 
💰 Narxi: {price} 
‍💻 Kasbi: {job} 
🕰 Murojaat qilish vaqti: {time}
🔎 Maqsad: {goal}
#xodim {hashtag} #{area}
            '''
        wait_time.sleep(2)
        await bot.send_message(admin, message)
        await state.finish()
        await msg.answer('maumotlaringi adminga yuborildi 12-24 soat oralag\'ida kanalda e\'lon qilinadi',
                         reply_markup=ReplyKeyboardRemove())
    else:
        await state.finish()
        await msg.answer('malumotlaringiz qabul qilinmadi', reply_markup=ReplyKeyboardRemove())
        await msg.answer('Tanlang', reply_markup=frelencer)


@dp.callback_query_handler(freelencer.filter(item__name="sherik"))
async def get_talim_state(call: types.CallbackQuery):
    await call.message.answer(
        f"""
Sherik topish uchun ariza berish
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
        """, reply_markup=ReplyKeyboardRemove()
    )
    await call.answer(cache_time=60)
    await call.message.answer('ism va familayangizni kriiting')
    await Sherik_kerak.fullname.set()


@dp.message_handler(state=Sherik_kerak.fullname)
async def sherik_get_fullname(msg: types.Message, state: FSMContext):
    fullname = msg.text
    if len(fullname) >= 4:
        await state.update_data({
            'fullname': fullname
        })
        await msg.answer(
            """
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Python, Java, GO
            """
        )
        await Sherik_kerak.next()
    else:
        await msg.answer('ismingiz va familayingiz 5 ta harfdan ko\'p bo\'lishi lozim ')
        await Ustoz_state.fullname.set()
        await msg.answer('ism va familayangizni kriiting')


@dp.message_handler(state=Sherik_kerak.skill)
async def sherik_get_skill(msg: types.Message, state: FSMContext):
    skill = msg.text.title().split(',')
    await state.update_data({
        'skill': skill

    })
    await msg.answer('''
    🌐 Hudud: 

    Qaysi hududdansiz?
    Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.

            ''')
    await Sherik_kerak.next()


@dp.message_handler(state=Sherik_kerak.area)
async def sherik_get_hudud(msg: types.Message, state: FSMContext):
    area = msg.text
    await state.update_data({
        'area': area
    })
    await msg.answer('''
    💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
    ''')
    await Sherik_kerak.next()


@dp.message_handler(state=Sherik_kerak.price)
async def sherik_get_price(msg: types.Message, state: FSMContext):
    price = msg.text

    await state.update_data({
        'price': price
    })
    await msg.answer('''
    🕰 Murojaat qilish vaqti: 

    Qaysi vaqtda murojaat qilish mumkin?
    Masalan, 9:00 - 18:00
        ''')
    await Sherik_kerak.next()


@dp.message_handler(state=Sherik_kerak.time)
async def sherik_get_time(msg: types.Message, state: FSMContext):
    time = msg.text
    await state.update_data({
        'time': time
    })
    await msg.answer('''
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
    ''')
    await Sherik_kerak.next()


@dp.message_handler(state=Sherik_kerak.goal)
async def sherik_get_goal(msg: types.Message, state: FSMContext):
    goal = msg.text
    await state.update_data({
        'goal': goal
    })
    data = await state.get_data()
    fullname = data.get('fullname')
    skills = data.get('skill')
    skill = ','.join(skills)
    hashtag = ''
    for x in skills:
        hashtag += x.replace(x, ' #' + x)
    area = data.get('area')
    price = data.get('price')
    time = data.get('time')
    goal = data.get('goal')
    username = msg.from_user.username
    message = f'''
    Sherik kerak:

🏅 Sherik: {fullname}
📚 Texnologiya: {skill}
🇺🇿 Telegram: @{username}
🌐 Hudud: {area} 
💰 Narxi: {price} 
🕰 Murojaat qilish vaqti: {time}
🔎 Maqsad: {goal}
#sherik {hashtag} #{area}
    '''
    wait_time.sleep(2)
    await msg.answer(message)
    await msg.answer("malumotlaringizni to'g'riligiga ishonch hosil qiling! ", reply_markup=agree)
    await Sherik_kerak.next()


@dp.message_handler(state=Sherik_kerak.finish)
async def set_sherik_finish(msg: types.message, state: FSMContext):
    text = msg.text
    if text == 'Ha':
        data = await state.get_data()
        fullname = data.get('fullname')
        skills = data.get('skill')
        skill = ','.join(skills)
        hashtag = ''
        for x in skills:
            hashtag += x.replace(x, ' #' + x)
        area = data.get('area')
        price = data.get('price')
        time = data.get('time')
        goal = data.get('goal')
        username = msg.from_user.username
        message = f'''
    Sherik kerak:

🏅 Sherik: {fullname}
📚 Texnologiya: {skill}
🇺🇿 Telegram: @{username}
🌐 Hudud: {area} 
💰 Narxi: {price} 
🕰 Murojaat qilish vaqti: {time}
🔎 Maqsad: {goal}
#sherik {hashtag} #{area}
            '''
        wait_time.sleep(2)
        await bot.send_message(admin, message)
        await msg.answer('maumotlaringi adminga yuborildi 12-24 soat oralag\'ida kanalda e\'lon qilinadi',
                         reply_markup=ReplyKeyboardRemove())
        await state.finish()
    else:
        await state.finish()
        await msg.answer('malumotlaringiz qabul qilinmadi', reply_markup=ReplyKeyboardRemove())
        await msg.answer('Tanlang', reply_markup=frelencer)


@dp.callback_query_handler(freelencer.filter(item__name="shogird"))
async def shogird_get_talim_state(call: types.CallbackQuery):
    await call.message.answer(
        f"""
Shogird topish uchun ariza berish
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
        """, reply_markup=ReplyKeyboardRemove()
    )
    await call.answer(cache_time=60)
    await call.message.answer('ism va familayangizni kriiting')
    await Ustoz_state.fullname.set()


@dp.message_handler(state=Shogir_kerak.fullname)
async def shogird_get_fullname(msg: types.Message, state: FSMContext):
    fullname = msg.text
    if len(fullname) >= 5:
        await state.update_data({
            'fullname': fullname
        })
        await msg.answer('Yoshingizni kiriting')
        await Shogir_kerak.next()
    else:
        await msg.answer('ismingiz va familayingiz 5 ta harfdan ko\'p bo\'lishi lozim ')
        await Shogir_kerak.fullname.set()
        await msg.answer('ism va familayangizni kriiting')


@dp.message_handler(state=Shogir_kerak.age)
async def shogird_get_age(msg: types.Message, state: FSMContext):
    age = msg.text
    if age.isnumeric():
        await state.update_data({
            'age': age
        })

        await msg.answer(
            """
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Python, Java, GO
            """
        )
        await Shogir_kerak.next()
    else:
        await msg.answer('siz harf kiritdingiz')
        await Shogir_kerak.age.set()
        await msg.answer('yoshingizni kiriting')


@dp.message_handler(state=Shogir_kerak.skill)
async def shogird_get_skill(msg: types.Message, state: FSMContext):
    skill = msg.text.title().split(',')
    await state.update_data({
        'skill': skill

    })
    await msg.answer("""
📞 Telefon: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67

    """)
    await Shogir_kerak.next()


@dp.message_handler(state=Shogir_kerak.phone)
async def shogird_get_phone(msg: types.Message, state: FSMContext):
    if re.match(phone_number, msg.text):
        phone = msg.text
        await state.update_data({
            'phone': phone
        })
        await msg.answer('''
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.

        ''')
        await Shogir_kerak.next()

    else:
        await msg.answer('siz no\'tog\'ri shaklda kiritdingiz yoki harf kriitidingiz')
        await state.finish()
        await Shogir_kerak.phone.set()
        await msg.answer("""
📞 Telefon: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67

            """)


@dp.message_handler(state=Shogir_kerak.area)
async def shogird_get_hudud(msg: types.Message, state: FSMContext):
    area = msg.text
    await state.update_data({
        'area': area
    })
    await msg.answer('''
    💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
    ''')
    await Shogir_kerak.next()


@dp.message_handler(state=Shogir_kerak.price)
async def shogird_get_price(msg: types.Message, state: FSMContext):
    price = msg.text

    await state.update_data({
        'price': price
    })
    await msg.answer('''
        👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
        ''')
    await Shogir_kerak.next()


@dp.message_handler(state=Shogir_kerak.job)
async def shogird_get_job(msg: types.Message, state: FSMContext):
    job = msg.text
    await state.update_data({
        'job': job
    })
    await msg.answer('''
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
    ''')
    await Shogir_kerak.next()


@dp.message_handler(state=Shogir_kerak.time)
async def shogird_get_time(msg: types.Message, state: FSMContext):
    time = msg.text
    await state.update_data({
        'time': time
    })
    await msg.answer('''
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
    ''')
    await Shogir_kerak.next()


@dp.message_handler(state=Shogir_kerak.goal)
async def shogird_get_goal(msg: types.Message, state: FSMContext):
    goal = msg.text
    await state.update_data({
        'goal': goal
    })
    data = await state.get_data()
    fullname = data.get('fullname')
    age = data.get('age')
    skills = data.get('skill')
    skill = ','.join(skills)
    hashtag = ''
    for x in skills:
        hashtag += x.replace(x, ' #' + x)
    phone = data.get('phone')
    area = data.get('area')
    price = data.get('price')
    job = data.get('job')
    time = data.get('time')
    goal = data.get('goal')
    username = msg.from_user.username
    message = f'''
    Shogird kerak:

🎓 Shogird: {fullname}
🌐 Yosh: {age}
📚 Texnologiya: {skill}
🇺🇿 Telegram: @{username}
📞 Aloqa: {phone} 
🌐 Hudud: {area} 
💰 Narxi: {price} 
👨🏻‍💻 Kasbi: {job} 
🕰 Murojaat qilish vaqti: {time}
🔎 Maqsad: {goal}
#ustoz {hashtag} #{area}
    '''
    wait_time.sleep(2)
    await msg.answer(message)
    await msg.answer("malumotlaringizni to'g'riligiga ishonch hosil qiling! ", reply_markup=agree)
    await Shogir_kerak.next()


@dp.message_handler(state=Shogir_kerak.finish)
async def set_finish_shogird(msg: types.Message, state: FSMContext):
    text = msg.text
    if text == 'Ha':
        data = await state.get_data()
        fullname = data.get('fullname')
        age = data.get('age')
        skills = data.get('skill')
        skill = ','.join(skills)
        hashtag = ''
        for x in skills:
            hashtag += x.replace(x, ' #' + x)
        phone = data.get('phone')
        area = data.get('area')
        price = data.get('price')
        job = data.get('job')
        time = data.get('time')
        goal = data.get('goal')
        username = msg.from_user.username
        message = f'''
    Shogird kerak:

🎓 Shogird: {fullname}
🌐 Yosh: {age}
📚 Texnologiya: {skill}
🇺🇿 Telegram: @{username}
📞 Aloqa: {phone} 
🌐 Hudud: {area} 
💰 Narxi: {price} 
‍💻 Kasbi: {job} 
🕰 Murojaat qilish vaqti: {time}
🔎 Maqsad: {goal}
#ustoz {hashtag} #{area}
            '''
        wait_time.sleep(2)
        await bot.send_message(admin, message)
        await msg.answer('maumotlaringi adminga yuborildi 12-24 soat oralag\'ida kanalda e\'lon qilinadi',
                         reply_markup=ReplyKeyboardRemove())
        await state.finish()
    else:
        await state.finish()
        await msg.answer('malumotlaringiz qabul qilinmadi', reply_markup=ReplyKeyboardRemove())
        await msg.answer('Tanlang', reply_markup=frelencer)


@dp.callback_query_handler(freelencer.filter(item__name="xodim"))
async def get_talim_state(call: types.CallbackQuery):
    await call.message.answer(
        f"""
Ustoz topish uchun ariza berish
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
        """, reply_markup=ReplyKeyboardRemove()
    )
    await call.answer(cache_time=60)
    await call.message.answer('🎓 Idora nomi?')
    await Xodim_kerak.idora.set()


@dp.message_handler(state=Xodim_kerak.idora)
async def get_fullname(msg: types.Message, state: FSMContext):
    idora = msg.text

    await state.update_data({
        'idora': idora
    })
    await msg.answer(
        """
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Python, Java, GO
        """
    )
    await Xodim_kerak.next()


@dp.message_handler(state=Xodim_kerak.skill)
async def get_skill(msg: types.Message, state: FSMContext):
    skill = msg.text.title().split(',')
    await state.update_data({
        'skill': skill

    })
    await msg.answer("""
📞 Telefon: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67

    """)
    await Xodim_kerak.next()


@dp.message_handler(state=Xodim_kerak.phone)
async def get_phone(msg: types.Message, state: FSMContext):
    if re.match(phone_number, msg.text):
        phone = msg.text
        await state.update_data({
            'phone': phone
        })
        await msg.answer('''
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.

        ''')
        await Xodim_kerak.next()

    else:
        await msg.answer('siz no\'tog\'ri shaklda kiritdingiz yoki harf kriitidingiz')
        await state.finish()
        await Xodim_kerak.phone.set()
        await msg.answer("""
📞 Telefon: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67

            """)


@dp.message_handler(state=Xodim_kerak.area)
async def get_hudud(msg: types.Message, state: FSMContext):
    area = msg.text
    await state.update_data({
        'area': area
    })
    await msg.answer('''
    💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
    ''')
    await Xodim_kerak.next()


@dp.message_handler(state=Xodim_kerak.price)
async def get_price(msg: types.Message, state: FSMContext):
    price = msg.text

    await state.update_data({
        'price': price
    })
    await msg.answer('''
✍️Mas'ul ism sharifi?
        ''')
    await Xodim_kerak.next()


@dp.message_handler(state=Xodim_kerak.responsible)
async def get_job(msg: types.Message, state: FSMContext):
    responsible = msg.text
    await state.update_data({
        'responsible': responsible
    })
    await msg.answer('''
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
    ''')
    await Xodim_kerak.next()


@dp.message_handler(state=Xodim_kerak.time)
async def get_time(msg: types.Message, state: FSMContext):
    time = msg.text
    await state.update_data({
        'time': time
    })
    await msg.answer('''
🕰 Ish vaqtini kiriting?
    ''')
    await Xodim_kerak.next()


@dp.message_handler(state=Xodim_kerak.job_time)
async def get_job_time(msg: types.Message, state: FSMContext):
    job_time = msg.text
    await state.update_data({
        'job_time': job_time
    })
    await msg.answer('''
‼️ Qo`shimcha ma`lumotlar?
    ''')
    await Xodim_kerak.next()


@dp.message_handler(state=Xodim_kerak.addition)
async def get_xodim_goal(msg: types.Message, state: FSMContext):
    addition = msg.text
    await state.update_data({
        'addition': addition
    })
    data = await state.get_data()
    idora = data.get('idora')
    skills = data.get('skill')
    hashtag = ''
    for x in skills:
        hashtag += x.replace(x, ' #' + x)
    skill = ','.join(skills)
    phone = data.get('phone')
    area = data.get('area')
    price = data.get('price')
    responsible = data.get('responsible')
    time = data.get('time')
    job_time = data.get('job_time')
    addition = data.get('addition')
    username = msg.from_user.username
    message = f'''
Xodim kerak:

🏢 Idora: {idora}
📚 Texnologiya: {skill}
🇺🇿 Telegram: {username}
📞 Aloqa: {phone}
🌐 Hudud: {area} 
✍️ Mas'ul: {responsible}
🕰 Murojaat vaqti: {time}
🕰 Ish vaqti: {job_time}
💰 Maosh: {price}
‼️ Qo`shimcha: {addition}

#ishJoyi {hashtag} #{area}
    '''
    wait_time.sleep(2)
    await msg.answer(message)
    await msg.answer("malumotlaringizni to'g'riligiga ishonch hosil qiling! ", reply_markup=agree)
    await Xodim_kerak.next()


@dp.message_handler(state=Xodim_kerak.finish)
async def set_xodim_finish(msg: types.Message, state: FSMContext):
    text = msg.text
    if text == 'Ha':
        data = await state.get_data()
        idora = data.get('idora')
        skills = data.get('skill')
        hashtag = ''
        for x in skills:
            hashtag += x.replace(x, ' #' + x)
        skill = ','.join(skills)
        phone = data.get('phone')
        area = data.get('area')
        price = data.get('price')
        responsible = data.get('responsible')
        time = data.get('time')
        job_time = data.get('job_time')
        addition = data.get('addition')
        username = msg.from_user.username
        message = f'''
    Xodim kerak:

🏢 Idora: {idora}
📚 Texnologiya: {skill}
🇺🇿 Telegram: {username}
📞 Aloqa: {phone}
🌐 Hudud: {area} 
✍️ Mas'ul: {responsible}
🕰 Murojaat vaqti: {time}
🕰 Ish vaqti: {job_time}
💰 Maosh: {price}
‼️ Qo`shimcha: {addition}
#ishJoyi {hashtag} #{area}
            '''
        wait_time.sleep(2)
        await bot.send_message(admin, message)
        await msg.answer('maumotlaringi adminga yuborildi 12-24 soat oralag\'ida kanalda e\'lon qilinadi',
                         reply_markup=ReplyKeyboardRemove())
        await state.finish()
    else:
        await state.finish()
        await msg.answer('malumotlaringiz qabul qilinmadi', reply_markup=ReplyKeyboardRemove())
        await msg.answer('Tanlang', reply_markup=frelencer)
