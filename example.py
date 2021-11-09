import telebot
from telebot import types

bot = telebot.TeleBot('2082841531:AAGGrZ8tdMwcNaximIWu0d9nb-FRcPPOfQo')

@bot.message_handler(commands = ['start'])
def StartCommand(message):
	bot.send_message(message.chat.id, f'Добрый день! {message.from_user.first_name} {message.from_user.last_name}' )

@bot.message_handler(commands = ['info', 'get_info'])
def GetUserInfo(message):
	markup_inline = types.InlineKeyboardMarkup()
	item_yes = types.InlineKeyboardButton(text = 'Yes', callback_data = 'yes')
	item_no = types.InlineKeyboardButton(text="No", callback_data='no')

	markup_inline.add(item_yes, item_no)
	bot.send_message(message.chat.id, 'Do you wanna know anything about yourself?',
		reply_markup=markup_inline
	)


@bot.callback_query_handler(func = lambda call : True)
def answer(call):
	if call.data == 'yes':
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)

		item_id = types.KeyboardButton('My ID') # ID
		item_username = types.KeyboardButton('My username') # username

		markup_reply.add(item_id, item_username)
		bot.send_message(call.message.chat.id, 'Press one of the Buttons',
			reply_markup = markup_reply
		)
	if call.data == 'no':
		pass
@bot.message_handler(content = ['text'])
def GetText(message):
	if message.text == 'My ID':
		bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
	elif message.text == 'My username':
		bot.send_message(message.chat.id, f'Your username: {message.from_user.first_name} {message.from_user.last_name}')


bot.polling(none_stop = True, interval = 0)