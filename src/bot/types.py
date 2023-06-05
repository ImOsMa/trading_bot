from telebot import types

ADD_BYBIT_ACCOUNT = types.InlineKeyboardButton("Добавить Bybit User", callback_data="add_bybit_acc")
ADD_TINKOFF_INVEST_ACCOUNT = types.InlineKeyboardButton("Добавить Tinkoff User", callback_data="add_tinkoff_acc")
BYBIT_SERVICE = types.InlineKeyboardButton("Bybit", callback_data="bybit")
TINKOFF_SERVICE = types.InlineKeyboardButton("Tinkoff Invest", callback_data="tinkoff")

CRYPTO_CURRENCIES = types.InlineKeyboardButton("Курсы криптовалют", callback_data="currencies_bybit")
CREATE_ORDER_BYBIT = types.InlineKeyboardButton("Создать заявку", callback_data="create_order_bybit")
CHANGE_ORDER_BYBIT = types.InlineKeyboardButton("Изменить заявку", callback_data="change_order_bybit")
CANCEL_ORDER_BYBIT = types.InlineKeyboardButton("Отменить заявку", callback_data="cancel_order_bybit")
ORDER_INFO_BYBIT = types.InlineKeyboardButton("Информация по заявке", callback_data="order_info_bybit")
ORDER_LIST_BYBIT = types.InlineKeyboardButton("Список заявок", callback_data="order_list_bybit")
WALLET_BALANCE_BYBIT = types.InlineKeyboardButton("Баланс счета", callback_data="wallet_balance_bybit")
ACCOUNT_INFO_BYBIT = types.InlineKeyboardButton("Информация об аккаунте", callback_data="account_info_bybit")
INSTRUMENT_INFO_BYBIT = types.InlineKeyboardButton("Получить инфо об инструменте",
                                                   callback_data="instrument_info_bybit")

BACK_BYBIT_MENU = types.InlineKeyboardButton("Bybit меню", callback_data="bybit_menu")

CURRENCY_EXCHANGE = types.InlineKeyboardButton("Курсы валют", callback_data="currencies_tinkoff")
CREATE_ORDER_TINKOFF = types.InlineKeyboardButton("Создать заявку", callback_data="create_order_tinkoff")
CANCEL_ORDER_TINKOFF = types.InlineKeyboardButton("Отменить заявку", callback_data="cancel_order_tinkoff")
ORDER_INFO_TINKOFF = types.InlineKeyboardButton("Информация по заявке", callback_data="order_info_tinkoff")
ORDER_LIST_TINKOFF = types.InlineKeyboardButton("Список заявок", callback_data="order_list_tinkoff")
ACCOUNT_INFO_TINKOFF = types.InlineKeyboardButton("Информация об аккаунте", callback_data="account_info_tinkoff")
WALLET_BALANCE_TINKOFF = types.InlineKeyboardButton("Баланс счета", callback_data="wallet_balance_tinkoff")
CREATE_STOP_ORDER_TINKOFF = types.InlineKeyboardButton("Создать заявку", callback_data="create_stop_order_tinkoff")
STOP_ORDER_INFO_TINKOFF = types.InlineKeyboardButton("Создать заявку", callback_data="stop_order_info_tinkoff")
SHARE_DIVIDENDS_TINKOFF = types.InlineKeyboardButton("Дивиденды", callback_data="share_dividents_tinkoff")
SHARE_INFO_TINKOFF = types.InlineKeyboardButton("Информация по ценной бумаге", callback_data="share_info_tinkoff")

BACK_TINKOFF_MENU = types.InlineKeyboardButton("Tinkoff меню", callback_data="tinkoff_menu")


