import telebot
from telebot import types

bot = telebot.TeleBot('2082841531:AAGGrZ8tdMwcNaximIWu0d9nb-FRcPPOfQo')

my_orders_counter = 0

@bot.message_handler(commands = ['start'])
def StartCommand(message):
	markup_inline = types.ReplyKeyboardMarkup(resize_keyboard = True)
	
	item_menu = types.KeyboardButton(text = u'📋' + "Меню")
	item_basket = types.KeyboardButton(text = u'🛒' + 'Корзина')
	item_my_orders = types.KeyboardButton(text = u'📝' + 'Мои Заказы')
	item_checkout = types.KeyboardButton(text = u'🚘' + 'Оформить Заказ')

	markup_inline.add(item_menu, item_checkout, item_basket, item_my_orders)
	bot.send_message(message.chat.id, f'Добрый день! {message.from_user.first_name}',
		reply_markup=markup_inline
	)

@bot.message_handler(content_types = ['text'])
def answer(message):
	if message.text == u'📋' + "Меню":
		markup_inline = types.ReplyKeyboardMarkup(resize_keyboard = True)

		item_shaurma = types.KeyboardButton(text = 'Шаурма')
		item_burger = types.KeyboardButton(text = 'Бургеры')
		item_pizza = types.KeyboardButton(text = 'Пицца')
		item_juice = types.KeyboardButton(text = 'Напитки')
		item_fri = types.KeyboardButton(text = 'Картофель Фри')
		item_souces = types.KeyboardButton(text = 'Соусы')
		item_supplements = types.KeyboardButton(text = 'Добавки')

		markup_inline.add(item_shaurma, item_burger, item_pizza, 
		item_juice, item_fri, item_souces, item_supplements 
		)
		bot.send_message(message.chat.id, 'Nizami',
			reply_markup=markup_inline
		)

bot.polling(none_stop = True, interval = 0)