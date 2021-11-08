import telebot
from telebot import types

bot = telebot.TeleBot('2082841531:AAGGrZ8tdMwcNaximIWu0d9nb-FRcPPOfQo')

my_orders_counter = 0

@bot.message_handler(commands = ['start'])
def StartCommand(message):
	markup_inline = types.ReplyKeyboardMarkup(resize_keyboard = True)
	

	item_basket = types.InlineKeyboardButton(text = u'🛒' + 'Корзина', callback_data = 'basket')
	item_my_orders = types.InlineKeyboardButton(text = u'📝' + 'Мои Заказы', callback_data = 'my_orders')
	item_checkout = types.InlineKeyboardButton(text = u'🚘' + 'Оформить Заказ', callback_data = 'checkout')

	markup_inline.add(item_checkout, item_basket, item_my_orders)
	bot.send_message(message.chat.id, 'Добрый день!',
		reply_markup=markup_inline
	)

@bot.callback_query_handler(func = lambda call : True)
def FirstStep(message)


bot.polling(none_stop = True, interval = 0)