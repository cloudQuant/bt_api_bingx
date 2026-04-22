"""Tests for BingXExchangeData container."""

from __future__ import annotations

from bt_api_bingx.exchange_data import BingXExchangeData


class TestBingXExchangeData:
    """Tests for BingXExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = BingXExchangeData()

        assert exchange.exchange_name == "BINGX___SPOT"
        assert "bingx.com" in exchange.rest_url
