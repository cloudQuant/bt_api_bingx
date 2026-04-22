from __future__ import annotations

from typing import TYPE_CHECKING

from bt_api_base.balance_utils import simple_balance_handler

from bt_api_bingx.exchange_data import BingXExchangeDataSpot
from bt_api_bingx.feeds.live_bingx.spot import BingXRequestDataSpot

if TYPE_CHECKING:
    from bt_api_base.registry import ExchangeRegistry


def register_bingx(registry: ExchangeRegistry) -> None:
    registry.register_feed("BINGX___SPOT", BingXRequestDataSpot)
    registry.register_exchange_data("BINGX___SPOT", BingXExchangeDataSpot)
    registry.register_balance_handler("BINGX___SPOT", simple_balance_handler)
