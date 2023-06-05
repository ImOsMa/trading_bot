from src.bot.types import *


def check_tinkoff_menu(call, bot):
    if call.data == TINKOFF_SERVICE.callback_data or call.data == BACK_TINKOFF_MENU.callback_data:
        markup = types.InlineKeyboardMarkup()
        markup.row(CURRENCY_EXCHANGE, CREATE_ORDER_TINKOFF)
        markup.row(CANCEL_ORDER_TINKOFF, ORDER_INFO_TINKOFF)
        markup.row(ORDER_LIST_TINKOFF, ACCOUNT_INFO_TINKOFF)
        markup.row(WALLET_BALANCE_TINKOFF, CREATE_STOP_ORDER_TINKOFF)
        markup.row(STOP_ORDER_INFO_TINKOFF, SHARE_DIVIDENDS_TINKOFF)
        markup.row(STOP_ORDER_INFO_TINKOFF, SHARE_INFO_TINKOFF)
        bot.send_message(call.message.chat.id, "Tinkoff функционал:", reply_markup=markup)