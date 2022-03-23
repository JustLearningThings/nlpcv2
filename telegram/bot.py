import telebot

bot = telebot.TeleBot('5270168831:AAEESF_RE08EzWKpaqsRqi54m56yvyc3Scg')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome')

@bot.message_handler(commands=['me'])
def me(message):
    bot.reply_to(message, bot.get_me())

@bot.message_handler(regexp='-\w+')
def regexp(message):
    bot.reply_to(message, 'OK')

@bot.message_handler(func=lambda m: 'sigmoid' in m and 'love' in m)
def echo(message):
    bot.reply_to(message, 'I like you too!')

# stacking handler
# OR
greetings = ['hello', 'hi']
@bot.message_handler(regexp='--\w+')
@bot.message_handler(func=lambda m: m.text in greetings and '--' not in m.text)
def greet(message):
    bot.reply_to(message, 'hi!')

# multiple filters
# AND
@bot.message_handler(regexp='~\w+', func=lambda m: len(m.text) < 3)
def beep(message):
    bot.reply_to(message, 'beep')

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, message.text)

# message handlers filters:
# - commands
# - regexp
# - func
# - content_type
# - chat_types

@bot.message_handler(commands=['photo'])
def photo(message):
    bot.reply_to('Sending photo...')
    bot.send_photo(message.chat.id, 'https://lafeber.com/pet-birds/wp-content/uploads/2020/04/gamaliel-troubleson-u9PsLITXMCQ-unsplash-e1587001975887.jpg')

bot.infinity_polling()