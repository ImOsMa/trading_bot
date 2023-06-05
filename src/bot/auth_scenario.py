import http

from src.bot.types import *

from src.auth.auth import Auth
from src.auth.schemas import AccountAdd
from src.client.bybit_client import ByBitService
from src.client.tinkoff_client import TinkoffService


def check_user_services(message, bot):
    users = Auth.get_user_by_id(int(message.chat.id))
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    button_array = []

    if len(users) == 0:
        markup.add(ADD_BYBIT_ACCOUNT, ADD_TINKOFF_INVEST_ACCOUNT)
        bot.send_message(message.chat.id, "Выбери сервис:", reply_markup=markup)
    else:
        for user in users:
            if user.account_id.isdigit():
                button_array.append(TINKOFF_SERVICE)
            else:
                button_array.append(BYBIT_SERVICE)

        if len(button_array) == 1:
            if TINKOFF_SERVICE in button_array:
                button_array.append(ADD_BYBIT_ACCOUNT)
            elif BYBIT_SERVICE in button_array:
                button_array.append(ADD_TINKOFF_INVEST_ACCOUNT)
        markup.add(*button_array)
        bot.send_message(message.chat.id, "Выбери сервис:", reply_markup=markup)


def check_account(call, bot, account_user):
    if call.data == ADD_BYBIT_ACCOUNT.callback_data:
        account_user.type = "Bybit"
        msg = bot.send_message(call.message.chat.id, "Введите токен пользователя ByBit:")
        bot.register_next_step_handler(msg, add_token_text_step, bot, account_user)

    elif call.data == ADD_TINKOFF_INVEST_ACCOUNT.callback_data:
        account_user.type = "Tinkoff"
        msg = bot.send_message(call.message.chat.id, "Введите токен пользователя Tinkoff:")
        bot.register_next_step_handler(msg, add_token_text_step, bot, account_user)


def add_token_text_step(message, bot, account_user):
    try:
        account_user.token = message.text
        msg = bot.send_message(message.chat.id, "Введите идентификатор пользователя")
        bot.register_next_step_handler(msg, add_account_id_step, bot, account_user)
    except Exception as e:
        bot.reply_to(message, "Ошибка при вводе токена")


def add_account_id_step(message, bot, account_user):
    try:
        account_user.account_id = message.text
        if account_user.type == 'Bybit':
            add_bybit_account(message, bot, account_user)
        elif account_user.type == 'Tinkoff':
            add_tinkoff_account(message, bot, account_user)
    except Exception as e:
        bot.reply_to(message, "Ошибка при вводе идентификатора аккаунта")


def add_bybit_account(message, bot, account_user):
    token = account_user.token
    account_id = account_user.account_id

    add_user_success_text = "Аккаунт ByBit был успешно добавлен"
    add_user_error_text = "Ошибка при добавлении аккаунта ByBit"

    res, code = ByBitService.account_info(token, account_id)
    if code == http.HTTPStatus.OK:
        if res.get('updated_time') == "0":
            new_account = AccountAdd(id=int(message.chat.id), account_id=account_id, token=token)
            try:
                db_resp = Auth.add_new_account_for_user(new_account=new_account)
                if db_resp.get('status') == "success":
                    msg = bot.send_message(message.chat.id, add_user_success_text)
                    check_user_services(msg, bot)
                else:
                    msg = bot.send_message(message.chat.id, add_user_error_text)
                    check_user_services(msg, bot)
            except Exception as e:
                msg = bot.send_message(message.chat.id, add_user_error_text)
                bot.register_next_step_handler(msg, check_user_services, bot)
    else:
        raise Exception(res.message)


def add_tinkoff_account(message, bot, account_user):
    token = account_user.token
    account_id = account_user.account_id

    add_user_success_text = "Аккаунт Tinkoff был успешно добавлен"
    add_user_error_text = "Ошибка при добавлении аккаунта Tinkoff"
    try:
        res, code = TinkoffService.get_user_accounts(token)
        if code == http.HTTPStatus.OK and len(res) != 0 and res[0].get('id') == account_id:
            new_account = AccountAdd(id=int(message.chat.id), account_id=account_id, token=token)
            db_resp = Auth.add_new_account_for_user(new_account=new_account)
            if db_resp.get('status') == "success":
                msg = bot.send_message(message.chat.id, add_user_success_text)
                check_user_services(msg, bot)
            else:
                msg = bot.send_message(message.chat.id, add_user_error_text)
                check_user_services(msg, bot)
    except Exception as e:
        msg = bot.send_message(message.chat.id, add_user_error_text)
        check_user_services(msg, bot)

