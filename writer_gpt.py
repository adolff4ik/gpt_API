import telebot
import openai


bot = telebot.TeleBot("api_key")

openai.api_key = "api_key"

@bot.message_handler(commands=['start'])
def meeting_message(message):
    bot.send_message(message.chat.id, text="Hello, " + message.chat.first_name)

    bot.send_message(message.chat.id, text='''вам лише потрібно написати тему тексту,
а потім бот дасть вам готовий текст''')


@bot.message_handler(content_types=['text'])
def answer(message):

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": f"""
Уяви що ти письменник-копірайтер у великій компанії і напиши текст на тему:
{message.text}"""}
        ]
    )

    bot.send_message(message.chat.id, text=completion.choices[0].message.content)


bot.infinity_polling()