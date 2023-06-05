import http
from datetime import datetime, date

from src.auth.auth import Auth
from src.bot.types import *
from src.bot.types import BYBIT_SERVICE
from src.client.bybit_client import ByBitService


def get_bybit_account(message) -> dict:
    user_dict = {"account_id": "", "token": ""}
    users = Auth.get_user_by_id(int(message.chat.id))
    for user in users:
        if user.account_id.isdigit():
            continue
        user_dict['account_id'] = user.account_id
        user_dict['token'] = user.token
    return user_dict


def back_to_bybit_menu(message, bot, message_text):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(BACK_BYBIT_MENU)
    bot.send_message(message.chat.id, message_text, reply_markup=markup)


def check_bybit_menu(call, bot):
    if call.data == BYBIT_SERVICE.callback_data or call.data == BACK_BYBIT_MENU.callback_data:
        markup = types.InlineKeyboardMarkup()
        markup.row(CRYPTO_CURRENCIES, CREATE_ORDER_BYBIT)
        markup.row(WALLET_BALANCE_BYBIT, ACCOUNT_INFO_BYBIT)
        markup.row(CHANGE_ORDER_BYBIT, ORDER_LIST_BYBIT)
        markup.row(ORDER_INFO_BYBIT, CANCEL_ORDER_BYBIT)
        markup.row(INSTRUMENT_INFO_BYBIT)
        bot.send_message(call.message.chat.id, "Bybit функционал:", reply_markup=markup)
    elif call.data == CRYPTO_CURRENCIES.callback_data:
        msg = bot.send_message(call.message.chat.id, "Введите символ (прим: BTCUSDT):")
        bot.register_next_step_handler(msg, add_symbol_currency, bot, get_bybit_account(msg))

    elif call.data == WALLET_BALANCE_BYBIT.callback_data:
        msg = bot.send_message(call.message.chat.id, "Баланс по счету")
        spot_wallet_balance(msg, bot, get_bybit_account(msg))

    elif call.data == CREATE_ORDER_BYBIT.callback_data:
        order_data = {'symbol': '', 'qty': '', 'side': '', 'type': '', 'price': None}
        msg = bot.send_message(call.message.chat.id, "Введите символ (прим: BTCUSDT):")
        bot.register_next_step_handler(msg, add_symbol_for_order, bot, get_bybit_account(msg), order_data)

    elif call.data == ORDER_INFO_BYBIT.callback_data:
        msg = bot.send_message(call.message.chat.id, "Введите ID заказа (прим: 1436047161193151232):")
        bot.register_next_step_handler(msg, add_order_id_for_get_order, bot, get_bybit_account(msg))

    elif call.data == ORDER_LIST_BYBIT.callback_data:
        msg = bot.send_message(call.message.chat.id, "Введите лимит на список заказов (прим: 5):")
        bot.register_next_step_handler(msg, add_limit_for_orders_list, bot, get_bybit_account(msg))

    elif call.data == ACCOUNT_INFO_BYBIT.callback_data:
        msg = bot.send_message(call.message.chat.id, "Данные аккаунта")
        get_user_info(msg, bot, get_bybit_account(msg))

    elif call.data == CANCEL_ORDER_BYBIT.callback_data:
        msg = bot.send_message(call.message.chat.id, "Введите ID заказа (прим: 1436047161193151232):")
        bot.register_next_step_handler(msg, delete_order, bot, get_bybit_account(msg))

    elif call.data == INSTRUMENT_INFO_BYBIT.callback_data:
        pass

    elif call.data == CHANGE_ORDER_BYBIT.callback_data:
        pass


def add_symbol_currency(message, bot, account):
    try:
        symbol = message.text
        res, code = ByBitService.get_coin_info(symbol, account.get('token'), account.get('account_id'))
        if code == http.HTTPStatus.BAD_REQUEST or code == http.HTTPStatus.INTERNAL_SERVER_ERROR:
            msg = bot.send_message(message.chat.id, f'Ошибка: {res.get("message")}\n'
                                                    f'Введите значение заново')
            bot.register_next_step_handler(msg, add_symbol_currency, bot, get_bybit_account(msg))
        message_text = f'Курс {res.get("symbol")}\n' \
                       f'Макс. цена покупателя: {res.get("bid")}\n'\
                       f'Мин. цена продавца: {res.get("ask")}'
        back_to_bybit_menu(message, bot, message_text)
    except Exception as e:
        bot.reply_to(message, "Ошибка при вводе символа")


def spot_wallet_balance(message, bot, account):
    try:
        res, code = ByBitService.spot_wallet_balance(account.get('token'), account.get('account_id'))
        if code == http.HTTPStatus.BAD_REQUEST or code == http.HTTPStatus.INTERNAL_SERVER_ERROR:
            back_to_bybit_menu(message, bot, f'Ошибка: {res.get("message")}\n')
        for coin in res:
            msg = bot.send_message(message.chat.id, f'Валюта {coin.get("coin")}\n'
                                                    f'Total: {coin.get("total")}\n'
                                                    f'Locked: {coin.get("locked")}\n')
        back_to_bybit_menu(msg, bot, "Баланс по криптовалютам получен")
    except Exception as e:
        bot.reply_to(message, "Ошибка при получении баланса")


def add_symbol_for_order(message, bot, account, order_data):
    try:
        order_data['symbol'] = message.text
        msg = bot.send_message(message.chat.id, "Введите количество лотов (прим: 2):")
        bot.register_next_step_handler(msg, add_qty_for_order, bot, account, order_data)
    except Exception as e:
        bot.reply_to(message, "Ошибка при вводе символа")
        back_to_bybit_menu(message, bot, "Ошибка при создании заказа")


def add_qty_for_order(message, bot, account, order_data):
    try:
        order_data['qty'] = float(message.text)
        msg = bot.send_message(message.chat.id, "Введите вид заказа (прим: Buy или Sell):")
        bot.register_next_step_handler(msg, add_side_for_order, bot, account, order_data)
    except Exception as e:
        bot.reply_to(message, "Ошибка при вводе количества")
        back_to_bybit_menu(message, bot, "Ошибка при создании заказа")


def add_side_for_order(message, bot, account, order_data):
    try:
        order_data['side'] = message.text
        msg = bot.send_message(message.chat.id, "Введите тип заказа (прим: LIMIT или MARKET):")
        bot.register_next_step_handler(msg, add_type_for_order, bot, account, order_data)
    except Exception as e:
        bot.reply_to(message, "Ошибка при вводе вида заказа")
        back_to_bybit_menu(message, bot, "Ошибка при создании заказа")


def add_type_for_order(message, bot, account, order_data):
    try:
        order_data['type'] = message.text
        if order_data['type'] == 'LIMIT':
            msg = bot.send_message(message.chat.id, "Введите цену заказа (прим: 21345):")
            bot.register_next_step_handler(msg, add_price_for_order, bot, account, order_data)
        else:
            msg = bot.send_message(message.chat.id, "Происходит создание заказа")
            post_spot_order(msg, bot, account, order_data)
    except Exception as e:
        bot.reply_to(message, "Ошибка при вводе типа заказа")
        back_to_bybit_menu(message, bot, "Ошибка при создании заказа")


def add_price_for_order(message, bot, account, order_data):
    try:
        order_data['price'] = float(message.text)
        msg = bot.send_message(message.chat.id, "Происходит создание заказа")
        post_spot_order(msg, bot, account, order_data)
    except Exception as e:
        bot.reply_to(message, "Ошибка при вводе типа заказа")
        back_to_bybit_menu(message, bot, "Ошибка при создании заказа")


def post_spot_order(message, bot, account, order_data):
    try:
        res, code = ByBitService.post_spot_order(order_data, account.get('token'), account.get('account_id'))
        if code == http.HTTPStatus.BAD_REQUEST or code == http.HTTPStatus.INTERNAL_SERVER_ERROR:
            back_to_bybit_menu(message, bot, f'Ошибка: {res.get("message")}\n')
        else:
            message_text = f'Заказ был создан!\n' \
                           f'ID заказа: {res.get("order_id")}\n' \
                           f'Криптовалюта: {res.get("symbol")}\n' \
                           f'Тип заказа: {res.get("type")}\n' \
                           f'Вид заказа: {res.get("side")}\n' \
                           f'Статус заказа: {res.get("status")}\n' \
                           f'Цена заказа: {res.get("price")}\n' \
                           f'Заявленное количество: {res.get("orig_qty")}\n' \
                           f'Совершенное количество: {res.get("executed_qty")}'
            back_to_bybit_menu(message, bot, message_text)
    except Exception as e:
        back_to_bybit_menu(message, bot, "Ошибка при создании заказа")


def add_order_id_for_get_order(message, bot, account):
    try:
        order_id = message.text
        res, code = ByBitService.get_spot_order(order_id, account.get('token'), account.get('account_id'))
        if code == http.HTTPStatus.BAD_REQUEST or code == http.HTTPStatus.INTERNAL_SERVER_ERROR:
            back_to_bybit_menu(message, bot, f'Ошибка: {res.get("message")}\n')
        else:
            message_text = f'Данные заказа!\n' \
                           f'ID заказа: {res.get("order_id")}\n' \
                           f'Криптовалюта: {res.get("symbol")}\n' \
                           f'Тип заказа: {res.get("type")}\n' \
                           f'Вид заказа: {res.get("side")}\n' \
                           f'Статус заказа: {res.get("status")}\n' \
                           f'Цена заказа: {res.get("price")}\n' \
                           f'Заявленное количество: {res.get("orig_qty")}\n' \
                           f'Совершенное количество: {res.get("executed_qty")}\n'
            back_to_bybit_menu(message, bot, message_text)
    except Exception as e:
        back_to_bybit_menu(message, bot, "Ошибка при получении данных о заказе")


def add_limit_for_orders_list(message, bot, account):
    try:
        limit = int(message.text)
        res, code = ByBitService.get_open_spot_orders(limit, account.get('token'), account.get('account_id'))
        if code == http.HTTPStatus.BAD_REQUEST or code == http.HTTPStatus.INTERNAL_SERVER_ERROR:
            back_to_bybit_menu(message, bot, f'Ошибка: {res.get("message")}\n')
        else:
            for order in res:
                message_text = f'Данные заказа!\n' \
                               f'ID заказа: {order.get("order_id")}\n' \
                               f'Криптовалюта: {order.get("symbol")}\n' \
                               f'Тип заказа: {order.get("type")}\n' \
                               f'Вид заказа: {order.get("side")}\n' \
                               f'Статус заказа: {order.get("status")}\n' \
                               f'Цена заказа: {order.get("price")}\n' \
                               f'Заявленное количество: {order.get("orig_qty")}\n' \
                               f'Совершенное количество: {order.get("executed_qty")}\n'
                msg = bot.send_message(message.chat.id, message_text)
            back_to_bybit_menu(msg, bot, "Данные по заказам получены")
    except Exception as e:
        back_to_bybit_menu(message, bot, "Ошибка при получении данных о заказах")


def get_user_info(message, bot, account):
    user_data = {"user_id": "", "margin_mode": "", "vip_level": "", "spot": [], "wallet": []}
    try:
        res, code = ByBitService.account_info(account.get('token'), account.get('account_id'))
        if code == http.HTTPStatus.BAD_REQUEST or code == http.HTTPStatus.INTERNAL_SERVER_ERROR:
            back_to_bybit_menu(message, bot, f'Ошибка: {res.get("message")}\n')
        else:
            user_data["margin_mode"] = res.get('margin_mode')

        res, code = ByBitService.key_information(account.get('token'), account.get('account_id'))
        if code == http.HTTPStatus.BAD_REQUEST or code == http.HTTPStatus.INTERNAL_SERVER_ERROR:
            back_to_bybit_menu(message, bot, f'Ошибка: {res.get("message")}\n')
        else:
            user_data["user_id"] = res.get('user_id')
            user_data['vip_level'] = res.get('vip_level')
            user_data['spot'] = res.get('permissions').get('spot')
            user_data['wallet'] = res.get('permissions').get('wallet')

        message_text = f'ID пользователя: {user_data["user_id"]}\n' \
                       f'Vip Level: {user_data["vip_level"]}\n' \
                       f'Margin Mode: {user_data["margin_mode"]}\n' \
                       f'Доступы на споте: {user_data["spot"]}\n' \
                       f'Доступы в кошельке: {user_data["wallet"]}'
        back_to_bybit_menu(message, bot, message_text)
    except Exception as e:
        back_to_bybit_menu(message, bot, "Ошибка при получении данных пользователя")


def delete_order(message, bot, account):
    try:
        order_id = message.text
        res, code = ByBitService.delete_spot_order(order_id, account.get('token'), account.get('account_id'))
        if code == http.HTTPStatus.BAD_REQUEST or code == http.HTTPStatus.INTERNAL_SERVER_ERROR:
            back_to_bybit_menu(message, bot, f'Ошибка: {res.get("message")}\n')
        message_text = f'Заказ был удален\n' \
                       f'ID заказа: {res.get("order_id")}\n' \
                       f'Статус: {res.get("status")}\n' \
                       f'Криптовалюта: {res.get("symbol")}\n' \
                       f'Тип заказа: {res.get("type")}\n' \
                       f'Вид заказа: {res.get("side")}\n'
        back_to_bybit_menu(message, bot, message_text)
    except Exception as e:
        back_to_bybit_menu(message, bot, "Не удалось удалить заказ")