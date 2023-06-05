import telebot
from src.bot.auth_scenario import check_user_services, check_account
from telebot.storage import StateMemoryStorage

from config import BOT_TOKEN
from src.bot.bybit_scenario import check_bybit_menu
from src.bot.tinkoff_scenario import check_tinkoff_menu


class User:
    def __int__(self, token_id, account_id):
        self.token = token_id
        self.account_id = account_id
        self.type = ""


account_user = User()


def main():
    state_storage = StateMemoryStorage()
    bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)

    @bot.message_handler(commands=["start"])
    def start_communication(message):
        bot.send_message(message.chat.id, "Привет! Представляю тебе бота Trading Robt! \n"
                                          "C помощью него ты можешь управлять активами ByBit или Тинькофф Инвестиции\n")
        check_user_services(message, bot)

    @bot.callback_query_handler(func=lambda call: True)
    def call_handler(call):
        check_account(call, bot, account_user)
        check_bybit_menu(call, bot)
        check_tinkoff_menu(call, bot)

    bot.infinity_polling()


if __name__ == '__main__':
    main()
