import telebot
from extensions import ConvertionException, CurrencyChecker
from config import keys, TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def guide(message: telebot.types.Message):
    text = '''Чтобы узнать текущий курс валюты, введите сообщение следующего формата:\n<имя валюты,\
 цену которой нужно узнать> <имя валюты, в которой надо узнать цену первой валюты>\
 <количество первой валюты (только целые значения)>\nПример:  доллар рубль 200
\nСписок всех доступных валют можно увидеть по команде /values'''
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) > 3:
            raise ConvertionException('Слишком много параметров. /help')

        if len(values) < 3:
            if len(values) == 2:
                if values[0] and values[1] in keys.keys():
                    values.append('1')
                elif values[0] in keys.keys() and values[1] not in keys.keys():
                    raise ConvertionException(f'Не удалось обработать валюту {values[1]}. /values')
                elif values[1] in keys.keys() and values[0] not in keys.keys():
                    raise ConvertionException(f'Не удалось обработать валюту {values[0]}. /values')
                else:
                    raise ConvertionException('Недостаточно параметров. /help')
            else:
                raise ConvertionException('Недостаточно параметров. /help')

        base, quote, amount = values
        total_base = CurrencyChecker.get_price(base, quote, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'{amount} {base} = {total_base} {quote}'
        bot.send_message(message.chat.id, text)


bot.polling()
