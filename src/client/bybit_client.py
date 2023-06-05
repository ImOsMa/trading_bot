import requests

BYBIT_URL = 'https://bybit-service.onrender.com'


class ByBitService:
    def __int__(self):
        pass

    @staticmethod
    def account_info(token, account_id):
        response = requests.get(f'{BYBIT_URL}/account/info', headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def spot_wallet_balance(token, account_id):
        response = requests.get(f'{BYBIT_URL}/account/spot_wallet_balance',
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def fee_rate(token, account_id):
        response = requests.get(f'{BYBIT_URL}/account/fee_rate',
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def key_information(token, account_id):
        response = requests.get(f'{BYBIT_URL}/account/key_information',
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def post_spot_order(data, token, account_id):
        response = requests.post(f'{BYBIT_URL}/order/post_spot_order', json=data,
                                 headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_spot_order(order_id, token, account_id):
        response = requests.get(f'{BYBIT_URL}/order/get_spot_order', params={'order_id': order_id},
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def delete_spot_order(order_id, token, account_id):
        response = requests.delete(f'{BYBIT_URL}/order/delete_spot_order', params={'order_id': order_id},
                                   headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_open_spot_orders(limit: int, token, account_id):
        response = requests.get(f'{BYBIT_URL}/order/open_spot_order', params={'limit': limit},
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def change_spot_order(data, token, account_id):
        response = requests.put(f'{BYBIT_URL}/order/change_order', json=data,
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_kline(symbol, interval, token, account_id):
        response = requests.get(f'{BYBIT_URL}/market/get_kline', params={'symbol': symbol, 'interval': interval},
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_instrument_info(symbol, token, account_id):
        response = requests.get(f'{BYBIT_URL}/market/instrument_info', params={'symbol': symbol},
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_tickers(symbol, token, account_id):
        response = requests.get(f'{BYBIT_URL}/market/tickers', params={'symbol': symbol},
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_position_info(symbol, token, account_id):
        response = requests.get(f'{BYBIT_URL}/market/position_info', params={'symbol': symbol},
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code

    @staticmethod
    def get_coin_info(symbol, token, account_id):
        response = requests.get(f'{BYBIT_URL}/market/coin_info', params={'symbol': symbol},
                                headers={'token': token, 'account_id': account_id})
        resp = response.json()
        return resp, response.status_code
