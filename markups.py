from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#~~~~~~~~~~~~~~~~~~~~~~~~~~SUB MENU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

btnUrlChannel = InlineKeyboardButton(text="Подписаться➕", url="https://t.me/crazycoderspython")
btnUrlChannel2 = InlineKeyboardButton(text="Подписаться➕", url='https://t.me/woodcutter_payments')
btnDoneSub = InlineKeyboardButton(text="Я подписался✔", callback_data="subchanneldone")

btnAdminUrl = InlineKeyboardButton(text="👨‍💻Программист", url='https://t.me/notidiots')
btnPayments = InlineKeyboardButton(text="💸Администратор", url='https://t.me/lalfy606')
AboutMenu = InlineKeyboardMarkup(row_width=1)
AboutMenu.insert(btnAdminUrl)
AboutMenu.insert(btnPayments)

checkSubMenu = InlineKeyboardMarkup(row_width=1)
checkSubMenu.insert(btnUrlChannel)
checkSubMenu.insert(btnUrlChannel2)
checkSubMenu.insert(btnDoneSub)

#~~~~~~~~~~~~~~~~~~~~~~~~~~MAIN MENU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

btnProfile = KeyboardButton('👨‍💻 Личный Кабинет')
btnMoney = KeyboardButton('Заработать💸')
btnPayment = KeyboardButton('Платежка💳')
btnAbout = KeyboardButton('О боте📚')
back = KeyboardButton('⬅Назад')
adminmenu = KeyboardButton('Админка')

btnAcceptOut = InlineKeyboardButton("Да я уверен💰")

AcceptMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
AcceptMenu.add(btnAcceptOut).add(back)

backMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
backMenu.add(back)

btnOut = KeyboardButton("Вывести📤")
OutMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
OutMenu.add(btnOut).add(back)

MainAdmin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
MainAdmin.add(btnProfile).add(btnMoney, btnPayment).add(btnAbout, adminmenu)

MainMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
MainMenu.add(btnProfile).add(btnMoney, btnPayment).add(btnAbout)