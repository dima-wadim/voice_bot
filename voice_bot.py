import os
import telebot
from gtts import gTTS

# Замените 'YOUR_API_TOKEN' на ваш токен бота
API_TOKEN = 'YOUR_API_TOKEN'

bot = telebot.TeleBot(API_TOKEN)

def send_voice_message(chat_id, text):
    """
    Преобразует текст в голосовое сообщение и отправляет его.
    """
    tts = gTTS(text, lang='ru')
    temp_file = 'bot_voice.mp3'
    tts.save(temp_file)
    with open(temp_file, 'rb') as voice:
        bot.send_voice(chat_id, voice)
    os.remove(temp_file)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = "Привет! Отправь мне текст, и я превращу его в голосовое сообщение."
    send_voice_message(message.chat.id, welcome_text)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    try:
        # Получаем текст сообщения
        text = message.text

        # Преобразуем текст в голос с использованием gTTS
        tts = gTTS(text, lang='ru')

        # Сохраняем аудио во временный файл
        tts.save('voice.mp3')

        # Отправляем голосовое сообщение пользователю
        with open('voice.mp3', 'rb') as voice:
            bot.send_voice(message.chat.id, voice)

        # Удаляем временный файл
        os.remove('voice.mp3')
    except Exception as e:
        error_message = "Произошла ошибка: " + str(e)
        send_voice_message(message.chat.id, error_message)

bot.polling()
