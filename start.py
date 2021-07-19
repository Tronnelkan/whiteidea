from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from data.config import admins
from keyboards.default.start_keyboard import start_keyboard
from loader import dp, bot
from states.start_state import StartState


@dp.message_handler(Command('start'))
async def hello(message: types.Message):
    await message.answer('Приветствуем вас в нашем магазине <b>WhiteIdea</b>\n'
                         'Мы магазин который продает курсы для каждого вида деятельности:\n'
                         '<b>🧑‍💻Програмирования🧑‍💻</b>\n'
                         '<b>👩‍🎨Дизайн👩‍🎨</b>\n'
                         '<b>👨‍💼Продвижения в социальных сетях👨‍💼</b>, и много всего другого\n'
                         'Пройдите регистрацию перед использыванием\n'
                         'Как вас зовут?')
    await StartState.one.set()


@dp.message_handler(state=StartState.one)
async def email(message: types.Message, state: FSMContext):
    name = message.text
    async with state.proxy() as data:
        data['name1'] = name
    await message.answer(f'{name} ✉️напишите свою gmail.com почту✉️')
    await StartState.next()


@dp.message_handler(Text(endswith='@gmail.com'), state=StartState.two)
async def description(message: types.Message, state: FSMContext):
    email = message.text
    async with state.proxy() as data:
        data['email1'] = email
    await message.answer('📲Обратная связь : @Crickettt777📲',
                         reply_markup=start_keyboard)
    await StartState.next()


@dp.message_handler(state=StartState.two)
async def not_email(message: types.Message, state: FSMContext):
    await message.answer('😁Напишите в формате gmail!😁')


@dp.message_handler(text='Закончить регистрацию', state=StartState.three)
async def description(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name_ad = data.get('name1')
    email = data.get('email1')
    await message.answer('Вы успешно зарегистрировались в нашем магазине теперь вы можете делать покупки👍\n'
                         'Нажмите /shop, чтобы попасть на страницу магазина')
    await bot.send_message(chat_id=863325996, text=f'😋Новый пользователь😋\n'
                                                f'<b>Имя : {name_ad}</b>\n'
                                                f'<b>Електронная почта : {email}</b>')
    await state.finish()


@dp.message_handler(state=StartState.three)
async def not_button(message: types.Message, state: FSMContext):
    await message.answer('😁Нажмите кнопку чтобы закончить регистрацию😁')
