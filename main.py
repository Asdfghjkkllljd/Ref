from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import markups as nav
from db import Database
import time
import config as cfg
from config import TOKEN
import time
import random
from random import randint
#не трогать !
CHANNEL_ID = '@extremecasinoo'
#не трогать !











CHANNEL_ID_2 = '@twinky0000'

num = "G.D-" + "{0}".format(randint(0, 100))

TOKEN = '7429518608:AAFMU2R_CyyLqPhWl2LJTWxTQVPU1DhSppk' #из #BotFather

Bot = Bot(token=TOKEN)
dp = Dispatcher(Bot)
db = Database('database.db')

online = 'Бот вышел в онлайн'
admin = '992835747'


async def on_startup(_):
    print(online)

def check_sub_channel(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    else:
        return False

@dp.message_handler(commands=['start'])
async def getstart(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            start_command = message.text
            referrer_id = str(start_command[7:])
            if str(referrer_id) != "":
                if str(referrer_id) != str(message.from_user.id):
                    db.add_user(message.from_user.id, referrer_id)
                    try:
                        await Bot.send_message(referrer_id, "<b>По вашей ссылке зарегистрировался 1 человек👥</b>", parse_mode='HTML')
                    except:
                        pass
                else:
                    db.add_user(message.from_user.id)
                    await Bot.send_message(message.from_user.id, "<b>🎭Нельзя регистрироваться по своей ссылке🎭 !</b>", parse_mode='HTML')

            else:
                db.add_user(message.from_user.id)
    if check_sub_channel(await Bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await Bot.send_message(message.from_user.id, "<b>🥁Добро пожаловать🥁!\n--------------\nПриглашай друзей и получай деньги💸\n1 привлеченный пользователь👥 = 0.40₽\n--------------\n💎Продается рекламное место подробнее @NotIdiots💎</b>", parse_mode='HTML', reply_markup=nav.MainMenu)
    else:
        await Bot.send_message(message.from_user.id, "<b>📓Подпишитесь на канал для использования бота!📓</b> ", parse_mode='HTML', reply_markup=nav.checkSubMenu)


@dp.message_handler(commands='setpay')
async def setpay(message: types.Message):
    if 'P' in message.text:
        text = message.text[8:]
        db.set_payments(message.from_user.id, text)
        db.set_signup(message.from_user.id, "done")
        user_pay = "🅿️Ваша платежка: " + db.get_payments(message.from_user.id)
        await Bot.send_message(message.from_user.id, f"<b>Ваша платежка установлена !\n\n{user_pay}</b> ", parse_mode='HTML')
    else:
        await message.reply("<b>Введите ваш PAYEER счет !</b>", parse_mode='HTML')



@dp.message_handler(commands=['sendall'])
async def get_all(message: types.Message):
    if message.chat.type == 'private':
        if (message.from_user.id == айди админа):
            text = message.text[9:]
            users = db.get_user()
            for row in users:
                try:
                    await Bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    pass
    if (message.from_user.id == айди админа):
        await Bot.send_message(message.from_user.id, "<b>Успешная рассылка !</b>", parse_mode='HTML')
    else:
        await Bot.send_message(message.from_user.id, "Ты не админ")


@dp.message_handler()
async def keyboards(message: types.Message):
    if message.text == '👨‍💻 Личный Кабинет':
        user_pay = "🅿️Ваша платежка: " + db.get_payments(message.from_user.id)
        await Bot.send_message(message.from_user.id, f"<b>Вы в 👨‍💻 Личном Кабинете \n\n 🆔Ваш ID: {message.chat.id} \n🕵️Ваше полное имя: {message.from_user.first_name} \n 🆔Уникальный ID: {num}{message.chat.id} \n\n👥Привлеченные пользователи: {db.count_reeferals(message.from_user.id)} \n👤Вас привел: {db.get_referrer(message.from_user.id)}\n\n📮Ваша реферальная ссылка:  Главное меню ➡ Заработать  \n{user_pay}</b> ", parse_mode='HTML', reply_markup=nav.OutMenu)
    if message.text == 'Вывести📤':
        await Bot.send_message(message.from_user.id, f"<b>⚔Вывод с 2 ₽ \n\n📮На кассе: 10 ₽\n👥Привлеченные пользователи: {db.count_reeferals(message.from_user.id)} \n\nВы уверены вывести ?</b> ", reply_markup=nav.AcceptMenu, parse_mode='HTML')
    if message.text == 'Да я уверен💰':
        if db.count_reeferals(message.from_user.id):
            await Bot.send_message(message.from_user.id, f"<b>Отлично ! ваша заявка отправлена ожидайте с вами свяжется администрация </b>", reply_markup=nav.MainMenu, parse_mode='HTML')
            await Bot.send_message(admin, f"<b> Пришла заявка ! \n\nUsername: {message.from_user.mention} \nID USER: {message.chat.id} \n\nБыстрее выведи !</b> ", parse_mode='HTML')
        else: # db.count_reeferals(0):
            await Bot.send_message(message.from_user.id, "<b> К сожадению у вас нет привлеченных партнеров😔 </b>", parse_mode='HTML')

    if message.text == 'Заработать💸':
        await Bot.send_message(message.from_user.id, f"<b>1 реферал👥 = 0.40 ₽ \n\nВаша реферальная ссылка🗣: https://t.me/{cfg.BOT_NICKNAME}?start={message.from_user.id}</b> ", reply_markup=nav.backMenu, parse_mode='HTML')
    if message.text == 'Платежка💳':
        await Bot.send_message(message.from_user.id, f"<b> Платежка только PAYEER !\nЧтобы установить реквизит /setpay [Ваш счет payeer]  в таком формате🏆 </b>", parse_mode='HTML')
    if message.text == 'О боте📚':
        await Bot.send_message(message.from_user.id, f"<b>Бот создан🤖: 29.05.22 </b>", parse_mode='HTML', reply_markup=nav.AboutMenu)
    if message.text == '⬅Назад':
        await Bot.send_message(message.from_user.id, f"<b>Вы в главном меню🛡</b>", reply_markup=nav.MainMenu, parse_mode='HTML')


@dp.callback_query_handler(text="subchanneldone")
async def subchanneldone(message: types.Message):
    await Bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await Bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await Bot.send_message(message.from_user.id, "<b>🥁Добро пожаловать🥁!\n---------------\nПриглашай друзей и получай деньги💸\n1 привлеченный пользователь👥 = 0.30 ₽\n--------------\n💎Продается рекламное место подробнее @NotIdiots💎</b>", parse_mode='HTML', reply_markup=nav.MainMenu)
    else:
        await Bot.send_message(message.from_user.id, "<b>📓Подпишитесь на канал для использования бота!📓</b> ", parse_mode='HTML', reply_markup=nav.checkSubMenu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

