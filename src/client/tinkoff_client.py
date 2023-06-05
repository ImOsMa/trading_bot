import requests

TINKOFF_URL = 'https://tinkoff-service.onrender.com'


class TinkoffService:
    def __int__(self):
        pass

    @staticmethod
    def get_operations(token, account_id):
        response = requests.get(f'{TINKOFF_URL}/operation_market/operations',
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_portfolio(token, account_id):
        response = requests.get(f'{TINKOFF_URL}/operation_market/portfolio',
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_positions(token, account_id):
        response = requests.get(f'{TINKOFF_URL}/operation_market/positions',
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_broker_report(token, account_id):
        response = requests.get(f'{TINKOFF_URL}/operation_market/broker_report',
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_withdraw_limits(token, account_id):
        response = requests.get(f'{TINKOFF_URL}/operation_market/withdraw_limits',
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_last_prices(figi, token):
        response = requests.get(f'{TINKOFF_URL}/operation_market/last_prices', params={'figi': figi},
                                headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_close_prices(figi, token):
        response = requests.get(f'{TINKOFF_URL}/operation_market/close_prices', params={'figi': figi},
                                headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_order_book(figi, depth: int, token):
        response = requests.get(f'{TINKOFF_URL}/operation_market/order_book',
                                params={'figi': figi, 'depth': depth}, headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_trading_schedules(exch, token):
        response = requests.get(f'{TINKOFF_URL}/user_instruments/trading_schedules',
                                params={'exch': exch}, headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_currencies(token):
        response = requests.get(f'{TINKOFF_URL}/user_instruments/currencies',
                                headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_currency_by(curr_id, token):
        response = requests.get(f'{TINKOFF_URL}/user_instruments/currency_by',
                                params={'id': curr_id}, headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def share_by(ticker, class_code, token):
        response = requests.get(f'{TINKOFF_URL}/user_instruments/share_by',
                                params={'ticker': ticker, 'class_code': class_code}, headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def shares(token):
        response = requests.get(f'{TINKOFF_URL}/user_instruments/shares',
                                headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def instrument_by(figi, token):
        response = requests.get(f'{TINKOFF_URL}/user_instruments/instrument_by',
                                params={'figi': figi}, headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def dividends(figi, token):
        response = requests.get(f'{TINKOFF_URL}/user_instruments/dividends',
                                params={'figi': figi}, headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_margin_attributes(token, account_id):
        response = requests.get(f'{TINKOFF_URL}/user_instruments/margin_attributes',
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_user_tariff(token):
        response = requests.get(f'{TINKOFF_URL}/user_instruments/user_tariff',
                                headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_user_info(token):
        response = requests.get(f'{TINKOFF_URL}/user_instruments/user_info', headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_user_accounts(token):
        response = requests.get(f'{TINKOFF_URL}/user_instruments/accounts', headers={'token': token})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def post_order(data, token, account_id):
        response = requests.post(f'{TINKOFF_URL}/orders/post_order', headers={'token': token, 'account_id': account_id},
                                 json=data)
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_order_state(order_id, token, account_id):
        response = requests.get(f'{TINKOFF_URL}/orders/order_state', headers={'token': token, 'account_id': account_id},
                                params={'order_id': order_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_orders(token, account_id):
        response = requests.get(f'{TINKOFF_URL}/orders/get', headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def post_cancel_order(order_id, token, account_id):
        response = requests.post(f'{TINKOFF_URL}/orders/cancel_order',
                                 headers={'token': token, 'account_id': account_id},
                                 params={'order_id': order_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def put_replace_order(data, token, account_id):
        response = requests.put(f'{TINKOFF_URL}/orders/replace_order',
                                headers={'token': token, 'account_id': account_id},
                                json=data)
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def post_stop_order(data, token, account_id):
        response = requests.post(f'{TINKOFF_URL}/orders/post_stop_order',
                                 headers={'token': token, 'account_id': account_id},
                                 json=data)
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_stop_orders(token, account_id):
        response = requests.get(f'{TINKOFF_URL}/orders/get_stop_order',
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def cancel_stop_order(order_id, token, account_id):
        response = requests.post(f'{TINKOFF_URL}/orders/post_stop_order',
                                 headers={'token': token, 'account_id': account_id},
                                 json={'stop_order_id': order_id})
        resp = response.json()
        return resp, response.status_code