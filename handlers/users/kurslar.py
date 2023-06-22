import re
import time as wait_time
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.menuKeyboards import menu, agree
from loader import dp, bot
from states.kurslar_state import Kurslar
phone_number = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
admin = 1091980088

@dp.message_handler(Text(equals="O'quv kurslari"))
async def get_talim_state(msg: types.Message):
    await msg.answer(
        f"""
O'quv kurlari  uchun ariza berish
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
        """, reply_markup=ReplyKeyboardRemove()
    )

    await msg.answer('🎓 Idora nomi?')
    await Kurslar.idora.set()


@dp.message_handler(state=Kurslar.idora)
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
    await Kurslar.next()


@dp.message_handler(state=Kurslar.skill)
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
    await Kurslar.next()


@dp.message_handler(state=Kurslar.phone)
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
        await Kurslar.next()

    else:
        await msg.answer('siz no\'tog\'ri shaklda kiritdingiz yoki harf kriitidingiz')
        await state.finish()
        await Kurslar.phone.set()
        await msg.answer("""
📞 Telefon: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67

            """)


@dp.message_handler(state=Kurslar.area)
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
    await Kurslar.next()


@dp.message_handler(state=Kurslar.price)
async def get_price(msg: types.Message, state: FSMContext):
    price = msg.text

    await state.update_data({
        'price': price
    })
    await msg.answer('''
✍️Mas'ul ism sharifi?
        ''')
    await Kurslar.next()


@dp.message_handler(state=Kurslar.responsible)
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
    await Kurslar.next()


@dp.message_handler(state=Kurslar.time)
async def get_time(msg: types.Message, state: FSMContext):
    time = msg.text
    await state.update_data({
        'time': time
    })
    await msg.answer('''
    ‼️ Afzalliklar haqida ma`lumotlar?
        ''')
    await Kurslar.next()




@dp.message_handler(state=Kurslar.addition)
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
    addition = data.get('addition')
    username = msg.from_user.username
    message = f'''
O'quv kurslar:

🎓 Idora: {idora}
📚 Texnologiya: {skill}
🇺🇿 Telegram: @{username}
📞 Aloqa: {phone}
✍️ Mas'ul: {responsible}
🌐 Hudud: {area}
💰 Narxi: {price}
🕰 Murojaat qilish vaqti: {time}
🎁 Afzalliklar: {addition}

#oquvKursi #{area} {hashtag}
    '''
    wait_time.sleep(2)
    await msg.answer(message)
    await msg.answer("malumotlaringizni to'g'riligiga ishonch hosil qiling! ", reply_markup=agree)
    await Kurslar.next()


@dp.message_handler(state=Kurslar.finish)
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
        addition = data.get('addition')
        username = msg.from_user.username
        message = f'''
O'quv kurslar:

🎓 Idora: {idora}
📚 Texnologiya: {skill}
🇺🇿 Telegram: @{username}
📞 Aloqa: {phone}
✍️ Mas'ul: {responsible}
🌐 Hudud: {area}
💰 Narxi: {price}
🕰 Murojaat qilish vaqti: {time}
🎁 Afzalliklar: {addition}

#oquvKursi #{area} {hashtag}
            '''
        wait_time.sleep(2)
        await bot.send_message(admin, message)
        await msg.answer('maumotlaringi adminga yuborildi 12-24 soat oralag\'ida kanalda e\'lon qilinadi',
                         reply_markup=ReplyKeyboardRemove())
        await msg.answer('Tanlang', reply_markup=menu)
        await state.finish()
    else:
        await state.finish()
        await msg.answer('malumotlaringiz qabul qilinmadi', reply_markup=ReplyKeyboardRemove())
        await msg.answer('Tanlang', reply_markup=menu)
