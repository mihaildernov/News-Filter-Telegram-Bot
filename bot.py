import requests
from bs4 import BeautifulSoup
from telegram.ext import *

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Здравствуй, пользователь!")

def read_url_contents(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            page_title = soup.title.string
            return f"Содержимое страницы: {page_title}"
        else:
            return "Не удалось получить содержимое страницы."
    except Exception as e:
        return f"Ошибка при получении содержимого страницы: {str(e)}"

def talk_to_me(update, context):
    message_text = update.message.text.lower()
    url = message_text
    page_content = read_url_contents(url)

    if "https" in message_text:
        #Если сообщение содержит ссылку, прочитаем ее содержимое
        update.message.reply_text(f"{page_content}\n{url}")

    try:

        if any(word in page_content for word in ["использовании", "употребление", "применение", "сферы деятельности", "облегчило", "экономика", "рынок", "условиях", "предотвратило", "контролирует", "шоу", "поиск"]):
            context.bot.forward_message(chat_id="-1001884988404", from_chat_id=update.message.chat_id,
                                    message_id=update.message.message_id)

        if any(word in page_content for word in ["создали", "начали", "разработали", "внедрили", "соорудили", "сделали"]):
            context.bot.forward_message(chat_id="-1001952569157", from_chat_id=update.message.chat_id,
                                    message_id=update.message.message_id)

        if any(word in page_content for word in ["компетенции", "навыки", "опыт", "научились", "смогли"]):
            context.bot.forward_message(chat_id="-1001896938675", from_chat_id=update.message.chat_id,
                                    message_id=update.message.message_id)

    except Exception as e:
        print(f"Error while forwarding message: {str(e)}")

def main():
    mybot = Updater("6550126209:AAFte6Wg5HbFWi9QovNrIjqbFeQ9QFMixLk", use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()
