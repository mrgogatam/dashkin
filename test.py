import pyowm
import telebot

owm = pyowm.OWM('1aff531da1c56a6eacaf429b11140462', language = "ru")
bot = telebot.TeleBot('1057671012:AAHVyUHX8naynNi4sKdemSXTv8jXjCZTC_Q')

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура: " + str(temp) + "\n"

	if temp < 5:
		answer += "Дюша, оденься тепло!"
	elif temp < 15:
		answer += "Даха, на улице прохладно, надень кофту!"
	else:
		answer += "Кисюк, на улице тепло!"

	bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True)