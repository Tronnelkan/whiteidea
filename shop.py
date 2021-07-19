import uuid

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hlink

from data import config
from data.items import items_instagram, items_youtube, items_selling, items_facebook, items_tiktok, items_telegram, \
    items_otviti
from keyboards.inline import shop_keyboard
from keyboards.inline.shop_keyboard import shop_keyboard, keyboard
from loader import dp
from utils.payments import Payment


@dp.message_handler(Command('shop'))
async def show_shop(message: types.Message):
    await message.answer('<b>🛒Страница магазина🛒</b>', reply_markup=shop_keyboard)


@dp.callback_query_handler(text_contains='back')
async def show_shop_but_inline(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer('<b>🛒Страница магазина🛒</b>', reply_markup=shop_keyboard)


@dp.callback_query_handler(text_contains='Instagram')
async def instagram(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.answer(cache_time=60)
    caption = """
    {title}
    <pre>{description}</pre>
    {price}
    """
    for item in items_instagram:
        await call.message.answer(caption.format(category=item.category, title=item.title, description=item.description,
                                                 price=item.price), reply_markup=keyboard(item_id=item.id))


@dp.callback_query_handler(text_contains='YouTube')
async def instagram(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.answer(cache_time=60)
    caption = """
    {title}
    <pre>{description}</pre>
    {price}
    """
    for item in items_youtube:
        await call.message.answer(
            caption.format(category=item.category, title=item.title, description=item.description, price=item.price),
            reply_markup=keyboard(item_id=item.id))


@dp.callback_query_handler(text_contains='Selling')
async def instagram(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.answer(cache_time=60)
    caption = """
    {title}
    <pre>{description}</pre>
    {price}
    """
    for item in items_selling:
        await call.message.answer(
            caption.format(category=item.category, title=item.title, description=item.description, price=item.price),
            reply_markup=keyboard(item_id=item.id))


@dp.callback_query_handler(text_contains='FaceBook')
async def instagram(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.answer(cache_time=60)
    caption = """
    {title}
    <pre>{description}</pre>
    {price}
    """
    for item in items_facebook:
        await call.message.answer(
            caption.format(category=item.category, title=item.title, description=item.description, price=item.price),
            reply_markup=keyboard(item_id=item.id))


@dp.callback_query_handler(text_contains='Telegram')
async def instagram(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.answer(cache_time=60)
    caption = """
    {title}
    <pre>{description}</pre>
    {price}
    """
    for item in items_telegram:
        await call.message.answer(
            caption.format(category=item.category, title=item.title, description=item.description, price=item.price),
            reply_markup=keyboard(item_id=item.id))


@dp.callback_query_handler(text_contains='TikTok')
async def instagram(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.answer(cache_time=60)
    caption = """
    {title}
    <pre>{description}</pre>
    {price}
    """
    for item in items_tiktok:
        await call.message.answer(
            caption.format(category=item.category, title=item.title, description=item.description, price=item.price),
            reply_markup=keyboard(item_id=item.id))


@dp.callback_query_handler(text_contains='Ot_viti')
async def instagram(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.answer(cache_time=60)
    caption = """
    {title}
    <pre>{description}</pre>
    {price}
    """
    for item in items_otviti:
        await call.message.answer(
            caption.format(category=item.category, title=item.title, description=item.description, price=item.price),
            reply_markup=keyboard(item_id=item.id))


@dp.callback_query_handler(text_contains='buy')
async def buy_payment(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    item_id = call.data.split(':')[-1]
    item_id = int(item_id) - 1
    item = items_instagram[item_id]
    amount = item.price
    comment = str(uuid.uuid4())

    payment = Payment(amount=amount, comment=comment)
    payment.create_comment()

    await call.message.answer(hlink(config.monobank, url=payment.invoice), disable_web_page_preview=True)
