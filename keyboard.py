from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup



def main_kb(user_id: int):
    kb_list = [
        [KeyboardButton(text="Расписание")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,resize_keyboard=True, one_time_keyboard=True)
    return keyboard


def course_kb_knt(user_id: int):
    course_list = [
        [InlineKeyboardButton(text='1 курс', callback_data='1course_knt')],
        [InlineKeyboardButton(text='Главное меню', callback_data='menu')]

    ]
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=course_list,resize_keyboard=True)
    return inline_keyboard


def faculty_kb(user_id: int):
    faculty_list = [
        [InlineKeyboardButton(text='КНТ', callback_data='knt')]
    ]
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=faculty_list, resize_keyboard=True)
    return inline_keyboard

def menu_kb(user_id: int):
    menu_list = [
        [InlineKeyboardButton(text='Главное меню', callback_data='menu')]
    ]
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=menu_list, resize_keyboard=True)
    return inline_keyboard

def knt_group_kb(user_id: int):
    knt_group_list = [
        [InlineKeyboardButton(text='КНТ-1', callback_data='knt1'),
         InlineKeyboardButton(text='КНТ-2', callback_data='knt2'),
         InlineKeyboardButton(text='КНТ-3', callback_data='knt3'),
         InlineKeyboardButton(text='КНТ-4', callback_data='knt4')],
        [InlineKeyboardButton(text='КНТ-5', callback_data='knt5'),
         InlineKeyboardButton(text='КНТ-6', callback_data='knt6'),
         InlineKeyboardButton(text='КНТ-7', callback_data='knt7'),],
        [InlineKeyboardButton(text='Главное меню', callback_data='menu')]
    ]
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=knt_group_list, resize_keyboard=True)
    return inline_keyboard

def week_kb(user_id: int):
    week_list = [
        [InlineKeyboardButton(text='Верхняя', callback_data='up'),
         InlineKeyboardButton(text='Нижняя', callback_data='down')],
        [InlineKeyboardButton(text='Главное меню', callback_data='menu')]
    ]
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=week_list, resize_keyboard=True)
    return inline_keyboard

def days_kb(user_id: int):
    days_list = [
        [InlineKeyboardButton(text='Пн', callback_data='monday'),
         InlineKeyboardButton(text='Вт', callback_data='tuesday'),
         InlineKeyboardButton(text='Ср', callback_data='wednesday')],
        [InlineKeyboardButton(text='Чт', callback_data='thursday'),
         InlineKeyboardButton(text='Пт', callback_data='friday'),
         InlineKeyboardButton(text='Сб', callback_data='saturday'),],
        [InlineKeyboardButton(text='Главное меню', callback_data='menu')]
    ]
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=days_list, resize_keyboard=True)
    return inline_keyboard