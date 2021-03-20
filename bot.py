import telebot

bot = telebot.TeleBot('1776983531:AAFye9U80n7xb-_y8QhBA2YcIONpWprUJdQ')

name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])

#@bot.message_handler(content_types=['text2'])

def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')

def get_text_messages(message):
	
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")

    elif message.text == "/help":
	    bot.send_message(message.from_user.id, "Напиши /Привет")

    else:
	    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(commands=['exchange'])  

def exchange_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('USD', callback_data='get-USD')  
    )  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'),  
        telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR')  
    )  
  
    bot.send_message(  
        message.chat.id,   
        'Click on the currency of choice:',  
        reply_markup=keyboard  
    )


bot.polling(none_stop=True, interval=0)




