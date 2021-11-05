import telebot
import configure

client = telebot.TeleBot(configure.config['2082841531:AAGGrZ8tdMwcNaximIWu0d9nb-FRcPPOfQo'])


client.polling(none_stop = True, interval = 0)
