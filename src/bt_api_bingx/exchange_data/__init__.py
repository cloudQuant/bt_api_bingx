from bt_api_base.containers.exchanges.exchange_data import ExchangeData


class BingXExchangeData(ExchangeData):
    def __init__(self):
        super().__init__()
        self.exchange_name = "BINGX___SPOT"
        self.rest_url = "https://open-api.bingx.com"
        self.wss_url = "wss://open-api-ws.bingx.com/market"
        self.rest_paths = {}
        self.wss_paths = {}
        self.kline_periods = {
            "1m": "1m",
            "3m": "3m",
            "5m": "5m",
            "15m": "15m",
            "30m": "30m",
            "1h": "1h",
            "2h": "2h",
            "4h": "4h",
            "6h": "6h",
            "12h": "12h",
            "1d": "1d",
            "3d": "3d",
            "1w": "1w",
            "1M": "1M",
        }
        self.legal_currency = ["USDT", "USD", "BTC", "ETH", "EUR"]

    def get_symbol(self, symbol):
        return symbol.upper()

    def get_period(self, period):
        return self.kline_periods.get(period, period)


class BingXExchangeDataSpot(BingXExchangeData):
    def __init__(self):
        super().__init__()
        self.asset_type = "spot"
        self.exchange_name = "BINGX___SPOT"
        self.rest_url = "https://open-api.bingx.com"
        self.rest_paths = {}


__all__ = ["BingXExchangeData", "BingXExchangeDataSpot"]
