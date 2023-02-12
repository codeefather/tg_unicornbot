import telebot
import openai

# api_key = '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'

bot = telebot.TeleBot('6176041343:AAHAJ6aobCJVJPdvLCrzXKf5jW7ryBO8CSc')
PROMPT = "unicorn anime"
api_key = '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'
openai.api_key = api_key
information_text = '"Привет. Меня создал кожанный мешок @peredozze для генерации изображений<br>Сейчас я настроен на генерацию по запросу: '

def createRequest():
    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="256x256",
    )
    return response


@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')
    bot.send_message(message.chat.id, information_text+PROMPT, parse_mode='html')

    # response = createRequest()

    # img_py = response["data"][0]["url"]

    # bot.send_photo(message.chat.id, img_py)

bot.polling(non_stop=True)
