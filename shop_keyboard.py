from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

shop_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Instagram', callback_data='Instagram'),
        InlineKeyboardButton(text='YouTube', callback_data='YouTube')
    ],
    [
        InlineKeyboardButton(text='Продажи', callback_data='Selling'),
        InlineKeyboardButton(text='FaceBook', callback_data='FaceBook')
    ],
    [
        InlineKeyboardButton(text='Telegram', callback_data='Telegram'),
        InlineKeyboardButton(text='TikTok', callback_data='TikTok')
    ],
    [
        InlineKeyboardButton(text='💪От Вити💪', callback_data='Ot_viti')
    ]
])


def keyboard(item_id):
    buy_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Купить', callback_data=f'buy:{item_id}')
        ],
        [
            InlineKeyboardButton(text='Главное меню', callback_data='back')
        ]
    ])
    return buy_keyboard


# back_to_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text='Назад', callback_data='back')
#     ]
# ])
