from .globals import *
from .lines import *
import telebot
import datetime
import threading

bot = telebot.TeleBot(token)  # Setting a token


# Processing /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, start_line)


# Processing /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, help_line)


# Processing /add_task
@bot.message_handler(commands=['add_task'])
def add_task_message(message):
    # Asking for a name of the task
    bot.send_message(message.chat.id, add_task_line)

    # Getting the name of the task, starting to initialize it
    bot.register_next_step_handler(message, task_name_init)


# Initializing the task
def task_name_init(message):
    date = {}  # The date which will be got from user
    date[message.chat.id] = {'task_name': message.text}

    # Asking for the task date
    bot.send_message(message.chat.id, task_init_line)

    # Getting the task date, starting to initialize the time
    bot.register_next_step_handler(message, task_time_init, date)


# Initializing the time
def task_time_init(message, date):
    # Converting the date into the format
    task_time = datetime.datetime.strptime(message.text, '%Y-%m-%d %H:%M:%S')

    now = datetime.datetime.now()  # Current date and time
    difference = task_time - now  # Difference for timer

    # Processing past date (an error)
    if difference.total_seconds() <= 0:
        bot.send_message(message.chat.id, error_line)
    else:
        # Sending a response
        task_name = date[message.chat.id]['task_name']
        bot.send_message(message.chat.id,
                         'Бот напомнит, что вам надо сделать'
                         ' следующее: "{}" в данное время: {}.'.format(
                             task_name, task_time))

        # Setting a timer
        task_timer = threading.Timer(difference.total_seconds(), send_task,
                                     [message.chat.id, task_name])
        task_timer.start()


# Sending a reminder for the task
def send_task(chat_id, task_name):
    bot.send_message(chat_id,
                     'Напоминание! Вам надо сделать следующее: "{}"'.format(
                         task_name))


# Processing a default message
@bot.message_handler(func=lambda message: True)
def default_message(message):
    bot.send_message(message.chat.id, default_line)


# Running the bot
def start():
    while True:
        bot.polling(none_stop=True)
