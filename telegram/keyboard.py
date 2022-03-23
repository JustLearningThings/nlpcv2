import telebot

bot = telebot.TeleBot('5270168831:AAEESF_RE08EzWKpaqsRqi54m56yvyc3Scg')
types = telebot.types

@bot.message_handler(func=lambda m: m.text in ['Google search', 'Github', 'Youtube'])
def go_to(message):
    if message.text == 'Google search':
        bot.reply_to(message, 'www.google.com')
    elif message.text == 'Github':
        bot.reply_to(message, 'www.github.com')
    elif message.text == 'Youtube':
        bot.reply_to(message, 'www.youtube.com')

# send_xyz
# optional argument: reply_markup
# reply_markup of types: ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply

markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
btn1 = types.KeyboardButton('Google search')
btn2 = types.KeyboardButton('Github')
btn3 = types.KeyboardButton('Youtube')
markup.add(btn1, btn2, btn3)

@bot.message_handler(commands=['go'])
def go(message):
    bot.send_message(message.chat.id, 'Where ?', reply_markup=markup)

markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
btn1 = types.KeyboardButton('Google search')
btn2 = types.KeyboardButton('Github')
btn3 = types.KeyboardButton('Youtube')
markup2.row(btn1)
markup2.row(btn2, btn3)

@bot.message_handler(commands=['go2'])
def go2(message):
    bot.send_message(message.chat.id, 'Where ?', reply_markup=markup2)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'cb_pizza':
        bot.answer_callback_query(call.id, 'Ordering pizza...')
    elif call.data == 'cb_pasta':
        bot.answer_callback_query(call.id, 'Ordering pasta...')
    else:
        bot.answer_callback_query(call.id, 'Something went wrong!')
    
    bot.send_message(call.from_user.id, 'Order placed.')

@bot.message_handler(func=lambda m: m.text.lower() == 'order')
def order(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton('Pizza', callback_data='cb_pizza')
    )
    markup.add(
        types.InlineKeyboardButton('Pasta', callback_data='cb_pasta')
    )

    bot.send_message(message.chat.id, 'Pizza or Pasta ?', reply_markup=markup)

bot.infinity_polling()