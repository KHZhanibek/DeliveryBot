import telebot

from telebot import types

bot = telebot.TeleBot('2082841531:AAGGrZ8tdMwcNaximIWu0d9nb-FRcPPOfQo')

@bot.message_handler(commands = ['start'])
def StartCommand(message):
	markup_inline = types.ReplyKeyboardMarkup(resize_keyboard = True)
	
	item_basket = types.InlineKeyboardButton(text = 'Корзина', callback_data = 'basket')
	item_my_orders = types.InlineKeyboardButton(text = 'Мои Заказы', callback_data = 'my_orders')
	item_checkout = types.InlineKeyboardButton(text = 'Оформить Заказ', callback_data = 'checkout')

	markup_inline.add(item_checkout, item_basket, item_my_orders)
	bot.send_message(message.chat.id, 'Добрый день!',
		reply_markup=markup_inline
	)

bot.polling(none_stop = True, interval = 0)

