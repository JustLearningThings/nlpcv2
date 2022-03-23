import telebot

bot = telebot.TeleBot('5270168831:AAEESF_RE08EzWKpaqsRqi54m56yvyc3Scg')
types = telebot.types

kitten_urls = [
    'https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80',
    'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F34%2F2018%2F05%2F12170411%2Fcat-kitten-138468381.jpg&q=60',
    'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F10%2F30%2Fkitten-in-a-blanket-153035391-2000.jpg'
]
kitten_url = 'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg'
rooster_url = 'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg'

@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result 1', types.InputTextMessageContent('Result message'))
        r2 = types.InlineQueryResultArticle('2', 'Result 2', types.InputTextMessageContent('Result message 2'))

        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'photo')
def photo(inline_query):
    try:
        r = types.InlineQueryResultPhoto('1', kitten_url, kitten_url, input_message_content=types.InputTextMessageContent('hi'))
        r2 = types.InlineQueryResultPhoto('2', rooster_url, rooster_url)

        bot.answer_inline_query(inline_query.id, [r, r2], cache_time=12)
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'kitten')
def kitten(inline_query):
    try:
        results = []

        for i, url in enumerate(kitten_urls):
            r = types.InlineQueryResultPhoto(str(i), url, url)

            results.append(r)
        
        bot.answer_inline_query(inline_query.id, results, cache_time=12)
    except Exception as e:
        print(e)

bot.infinity_polling()