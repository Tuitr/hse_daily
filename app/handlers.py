import os

from aiogram import html, Router, F, Bot
from aiogram.client import bot
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, CallbackQuery

from keyboard import *
from aiogram.types import ReplyKeyboardRemove

from app.pars import d

from answer.text import *
from dotenv import load_dotenv


router = Router()

group = ''
week = ''
day = ''
cb_week = ['up','down']
cb = ['knt', 'lawyer', 'mbk', 'menu']
cb_lawyer = ['1course_lawyer', '2course_lawyer', '3course_lawyer']
cb_mbk = ['1course_mbk', '2course_mbk', '3course_mbk']
cb_knt = ['1course_knt', '2course_knt', '3course_knt']
cb_knt_group_1 = ['knt1', 'knt2', 'knt3', 'knt4', 'knt5', 'knt6','knt7','menu']
cb_day = ['monday','tuesday','wednesday','thursday','friday','saturday']


@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.delete()
    await message.answer(f" {html.bold(message.from_user.full_name)}, добро пожаловать в HSE Daily! \n"
                         f"\n"
                         f"{hello}",
                         reply_markup=main_kb(message.from_user.id))


    user = message.from_user
    basic_info = {
        'chat_id': message.chat.id,
        'user_id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'is_premium': user.is_premium,
    }
    users = [x[:-1] for x in open('users.txt')]
    users_chat_id = [x[:-1] for x in open('users_chat_id.txt')]
    with open('users.txt', 'a', encoding='utf-8') as file:
        if f'{basic_info}' not in users:
            file.write(f'{basic_info}\n')
    with open('users_chat_id.txt', 'a', encoding='utf-8') as file:
        if f'{basic_info["chat_id"]}' not in users_chat_id:
            file.write(f'{basic_info["chat_id"]}\n')



@router.message(Command('spam'))
async def get_inline_course(message: Message, command: CommandObject,bot: Bot):
    if f'{message.from_user.id}' == f'{os.getenv("ADMIN_ID")}':
        spam_text = command.args
        with open('users_chat_id.txt', 'r') as file:
            for line in file:
                id = int(line.strip())
                await bot.send_message(chat_id=id,text=f'{spam_text}')
    else:
        await message.answer('Вы не являетесь администратором!')
        return


@router.message(F.text == 'Расписание')
async def get_inline_course(message: Message):
    msg = await message.answer('В процессе...', reply_markup=ReplyKeyboardRemove())
    await msg.delete()
    await message.answer("Выбери направлeние!",reply_markup=faculty_kb(message.from_user.id))


@router.callback_query(lambda callback: callback.data in cb)
async def callback_faculty(callback: CallbackQuery):
    if callback.data == 'knt':
        await callback.answer('Да здравствуют КНТшники!')
        await callback.message.edit_text('Выберите курс!', reply_markup=course_kb_knt(callback.from_user.id))
    elif callback.data == 'menu':
        await callback.answer('Вы вернулись в главное меню!')
        await callback.message.edit_text('Выбери направление!', reply_markup=faculty_kb(callback.from_user.id))


@router.callback_query(lambda callback: callback.data in cb_knt)
async def callback_knt(callback: CallbackQuery):
    if callback.data == '1course_knt':
        await callback.answer('')
        await callback.message.edit_text('Расписание первого курса', reply_markup=knt_group_kb(callback.from_user.id))


@router.callback_query(lambda callback: callback.data in cb_knt_group_1)
async def callback_group(callback: CallbackQuery):
    global group
    if callback.data == 'knt1':
        group = '1'
        await callback.answer('')
        await callback.message.edit_text('Выберите неделю!', reply_markup=week_kb(callback.from_user.id))
    elif callback.data == 'knt2':
        group = '2'
        await callback.answer('')
        await callback.message.edit_text('Выберите неделю!', reply_markup=week_kb(callback.from_user.id))
    elif callback.data == 'knt3':
        group = '3'
        await callback.answer('')
        await callback.message.edit_text('Выберите неделю!', reply_markup=week_kb(callback.from_user.id))
    elif callback.data == 'knt4':
        group = '4'
        await callback.answer('')
        await callback.message.edit_text('Выберите неделю!', reply_markup=week_kb(callback.from_user.id))
    elif callback.data == 'knt5':
        group = '5'
        await callback.answer('')
        await callback.message.edit_text('Выберите неделю!', reply_markup=week_kb(callback.from_user.id))
    elif callback.data == 'knt6':
        group = '6'
        await callback.answer('')
        await callback.message.edit_text('Выберите неделю!', reply_markup=week_kb(callback.from_user.id))
    elif callback.data == 'knt7':
        group = '7'
        await callback.answer('')
        await callback.message.edit_text('Выберите неделю!', reply_markup=week_kb(callback.from_user.id))
    elif callback.data == 'menu':
        await callback.answer('Вы вернулись в главное меню!')
        await callback.message.edit_text('Выбери направление!', reply_markup=faculty_kb(callback.from_user.id))
    return group


@router.callback_query(lambda callback: callback.data in cb_week)
async def callback_week(callback: CallbackQuery):
    global week
    if callback.data == 'up':
        week = 'up'
        await callback.answer('')
        await callback.message.edit_text('Выбери день!', reply_markup=days_kb(callback.from_user.id))
    elif callback.data == 'down':
        week = 'down'
        await callback.answer('')
        await callback.message.edit_text('Выбери день!', reply_markup=days_kb(callback.from_user.id))
    elif callback.data == 'menu':
        await callback.answer('Вы вернулись в главное меню!')
        await callback.message.edit_text('Выбери направление!', reply_markup=faculty_kb(callback.from_user.id))
    return week


@router.callback_query(lambda callback: callback.data)
async def callback_day(callback: CallbackQuery):
    global day
    global week
    global group
    if callback.data == 'monday':
        day = 'monday'
        await callback.answer('')
        await callback.message.edit_text(f'{d(group,week,day)}', reply_markup=menu_kb(callback.from_user.id))
    elif callback.data == 'tuesday':
        day = 'tuesday'
        await callback.answer('')
        await callback.message.edit_text(f'{d(group,week,day)}', reply_markup=menu_kb(callback.from_user.id))
    elif callback.data == 'wednesday':
        day = 'wednesday'
        await callback.answer('')
        await callback.message.edit_text(f'{d(group,week,day)}', reply_markup=menu_kb(callback.from_user.id))
    elif callback.data == 'thursday':
        day = 'thursday'
        await callback.answer('')
        await callback.message.edit_text(f'{english_today}', reply_markup=menu_kb(callback.from_user.id))
    elif callback.data == 'friday':
        day = 'friday'
        await callback.answer('')
        await callback.message.edit_text(f'{d(group,week,day)}', reply_markup=menu_kb(callback.from_user.id))
    elif callback.data == 'saturday':
        day = 'saturday'
        await callback.answer('')
        await callback.message.edit_text(f'{english_today}', reply_markup=menu_kb(callback.from_user.id))
    elif callback.data == 'menu':
        await callback.answer('Вы вернулись в главное меню!')
        await callback.message.edit_text('Выбери направление!', reply_markup=faculty_kb(callback.from_user.id))
    return day