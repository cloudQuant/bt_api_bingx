import json
import time
from typing import Any

from bt_api_base.containers.tickers.ticker import TickerData

from bt_api_bingx.tickers.ticker_utils import parse_float


class BingXRequestTickerData(TickerData):
    def __init__(
        self,
        ticker_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ):
        super().__init__(ticker_info, has_been_json_encoded)
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.exchange_name = "BINGX"
        self.local_update_time = time.time()
        self.ticker_data: dict[str, Any] | None = (
            ticker_info if has_been_json_encoded and isinstance(ticker_info, dict) else None
        )
        self.ticker_symbol_name = None
        self.last_price = None
        self.bid_price = None
        self.ask_price = None
        self.volume_24h = None
        self.high_24h = None
        self.low_24h = None
        self.open_24h = None
        self.has_been_init_data = False

    def init_data(self):
        if not self.has_been_json_encoded:
            self.ticker_data = json.loads(self.ticker_info)
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        data = self.ticker_data or {}
        data_list = data.get("data", [])
        data = data_list[0] if isinstance(data_list, list) and len(data_list) > 0 else {}

        if data:
            self.ticker_symbol_name = data.get("symbol")
            self.last_price = parse_float(data.get("lastPrice"))
            self.bid_price = parse_float(data.get("bidPrice"))
            self.ask_price = parse_float(data.get("askPrice"))
            self.volume_24h = parse_float(data.get("volume"))
            self.high_24h = parse_float(data.get("highPrice"))
            self.low_24h = parse_float(data.get("lowPrice"))
            self.open_24h = parse_float(data.get("openPrice"))

        self.has_been_init_data = True
        return self


__all__ = ["BingXRequestTickerData"]
