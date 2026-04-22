# bt_api_bingx

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_bingx.svg)](https://pypi.org/project/bt_api_bingx/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_bingx.svg)](https://pypi.org/project/bt_api_bingx/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_bingx/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_bingx/actions)
[![Docs](https://readthedocs.org/projects/bt-api-bingx/badge/?version=latest)](https://bt-api-bingx.readthedocs.io/)

---

<!-- English -->
# bt_api_bingx

> **BingX exchange plugin for bt_api** — Unified REST API for **Spot** trading with real-time market data.

`bt_api_bingx` is a runtime plugin for [bt_api](https://github.com/cloudQuant/bt_api_py) that connects to **BingX** exchange. It depends on [bt_api_base](https://github.com/cloudQuant/bt_api_base) for core infrastructure.

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-bingx.readthedocs.io/ |
| Chinese Docs | https://bt-api-bingx.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_bingx |
| PyPI | https://pypi.org/project/bt_api_bingx/ |
| Issues | https://github.com/cloudQuant/bt_api_bingx/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://github.com/cloudQuant/bt_api_py |

---

## Features

### 1 Asset Type

| Asset Type | Code | REST | WebSocket | Description |
|---|---|---|---|---|
| Spot | `BINGX___SPOT` | ✅ | — | Spot trading |

### REST API

- **Synchronous REST** — Polling for order management, balance queries, historical data
- **HMAC SHA256 signature** — Secure API authentication

### Plugin Architecture

Auto-registers at import time via `ExchangeRegistry`. Works seamlessly with `BtApi`:

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BINGX___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("BINGX___SPOT", "BTCUSDT")
balance = api.get_balance("BINGX___SPOT")
order = api.make_order(exchange_name="BINGX___SPOT", symbol="BTCUSDT", volume=0.001, price=50000, order_type="limit")
```

### Unified Data Containers

All exchange responses normalized to bt_api_base container types:

- `TickContainer` — 24hr rolling ticker
- `OrderBookContainer` — Order book depth
- `BarContainer` — K-line/candlestick
- `OrderContainer` — Order status and fills
- `AccountBalanceContainer` — Asset balances

---

## Installation

### From PyPI (Recommended)

```bash
pip install bt_api_bingx
```

### From Source

```bash
git clone https://github.com/cloudQuant/bt_api_bingx
cd bt_api_bingx
pip install -e .
```

### Requirements

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## Quick Start

### 1. Install

```bash
pip install bt_api_bingx
```

### 2. Get ticker (public — no API key needed)

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={})
ticker = api.get_tick("BINGX___SPOT", "BTCUSDT")
print(f"BTCUSDT price: {ticker}")
```

### 3. Place an order (requires API key)

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BINGX___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="BINGX___SPOT",
    symbol="BTCUSDT",
    volume=0.001,
    price=50000,
    order_type="LIMIT",
)
print(f"Order placed: {order}")
```

### 4. bt_api Plugin Integration

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BINGX___SPOT": {"api_key": "key", "secret": "secret"}
})

# REST calls
ticker = api.get_tick("BINGX___SPOT", "BTCUSDT")
balance = api.get_balance("BINGX___SPOT")
depth = api.get_depth("BINGX___SPOT", "BTCUSDT", count=20)
klines = api.get_kline("BINGX___SPOT", "BTCUSDT", period="1h", count=100)
```

---

## Architecture

```
bt_api_bingx/
├── src/bt_api_bingx/
│   ├── __init__.py                  # Package entry
│   ├── plugin.py                    # register_plugin() — bt_api plugin entry point
│   ├── registry_registration.py    # register_bingx() — feeds / exchange_data registration
│   ├── exchange_data/
│   │   └── __init__.py             # BingXExchangeData, BingXExchangeDataSpot
│   ├── feeds/
│   │   └── live_bingx/
│   │       ├── __init__.py
│   │       ├── request_base.py     # BingXRequestData base class
│   │       └── spot.py             # BingXRequestDataSpot
│   └── errors/
│       └── __init__.py
├── tests/
├── docs/
└── pyproject.toml
```

---

## Supported Operations

| Category | Operation | Notes |
|---|---|---|
| **Market Data** | `get_ticker` | 24hr rolling ticker |
| | `get_depth` | Order book depth |
| | `get_kline` | Intervals: 1m/3m/5m/15m/30m/1h/2h/4h/6h/12h/1d/3d/1w/1M |
| | `get_exchange_info` | Exchange trading rules and symbol info |
| **Account** | `get_balance` | All asset balances |
| | `get_account` | Full account info |
| **Trading** | `make_order` | LIMIT orders |
| | `cancel_order` | Cancel single order |
| | `query_order` | Query order by ID |
| | `get_open_orders` | All open orders |

---

## Supported BingX Symbols

All BingX Spot trading pairs are supported, including:

- **USDT pairs**: `BTCUSDT`, `ETHUSDT`, `SOLUSDT`, `XRPUSDT`, `BNBUSDT` ...
- **USD pairs**: `BTCUSD`, `ETHUSD`, `SOLUSD` ...
- **BTC pairs**: `ETHBTC`, `BNBBTC` ...
- **ETH pairs**: `BNBETH` ...
- **EUR pairs**: `BTCEUR`, `ETHEUR` ...

---

## Rate Limits

| Endpoint | Limit |
|---|---|
| Public endpoints | 200 requests/minute |
| Trade endpoints | 100 requests/minute |

---

## Documentation

| Doc | Link |
|-----|------|
| **English** | https://bt-api-bingx.readthedocs.io/ |
| **中文** | https://bt-api-bingx.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://cloudquant.github.io/bt_api_py/ |

---

## License

MIT — see [LICENSE](LICENSE).

---

## Support

- [GitHub Issues](https://github.com/cloudQuant/bt_api_bingx/issues) — bug reports, feature requests
- Email: yunjinqi@gmail.com

---

---

## 中文

> **bt_api 的 BingX 交易所插件** — 为**现货**交易提供统一的 REST API 和实时市场数据。

`bt_api_bingx` 是 [bt_api](https://github.com/cloudQuant/bt_api_py) 的运行时插件，连接 **BingX** 交易所。依赖 [bt_api_base](https://github.com/cloudQuant/bt_api_base) 提供核心基础设施。

| 资源 | 链接 |
|------|------|
| 英文文档 | https://bt-api-bingx.readthedocs.io/ |
| 中文文档 | https://bt-api-bingx.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_bingx |
| PyPI | https://pypi.org/project/bt_api_bingx/ |
| 问题反馈 | https://github.com/cloudQuant/bt_api_bingx/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://github.com/cloudQuant/bt_api_py |

---

## 功能特点

### 1 种资产类型

| 资产类型 | 代码 | REST | WebSocket | 说明 |
|---|---|---|---|---|
| 现货 | `BINGX___SPOT` | ✅ | — | 现货交易 |

### REST API

- **同步 REST** — 轮询方式处理订单管理、余额查询、历史数据
- **HMAC SHA256 签名** — 安全的 API 认证

### 插件架构

通过 `ExchangeRegistry` 在导入时自动注册，与 `BtApi` 无缝协作：

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BINGX___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("BINGX___SPOT", "BTCUSDT")
balance = api.get_balance("BINGX___SPOT")
order = api.make_order(exchange_name="BINGX___SPOT", symbol="BTCUSDT", volume=0.001, price=50000, order_type="limit")
```

### 统一数据容器

所有交易所响应规范化为 bt_api_base 容器类型：

- `TickContainer` — 24小时滚动行情
- `OrderBookContainer` — 订单簿深度
- `BarContainer` — K线/蜡烛图
- `OrderContainer` — 订单状态和成交
- `AccountBalanceContainer` — 资产余额

---

## 安装

### 从 PyPI 安装（推荐）

```bash
pip install bt_api_bingx
```

### 从源码安装

```bash
git clone https://github.com/cloudQuant/bt_api_bingx
cd bt_api_bingx
pip install -e .
```

### 系统要求

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## 快速开始

### 1. 安装

```bash
pip install bt_api_bingx
```

### 2. 获取行情（公开接口，无需 API key）

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={})
ticker = api.get_tick("BINGX___SPOT", "BTCUSDT")
print(f"BTCUSDT 价格: {ticker}")
```

### 3. 下单交易（需要 API key）

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BINGX___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="BINGX___SPOT",
    symbol="BTCUSDT",
    volume=0.001,
    price=50000,
    order_type="LIMIT",
)
print(f"订单已下单: {order}")
```

### 4. bt_api 插件集成

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BINGX___SPOT": {"api_key": "key", "secret": "secret"}
})

# REST 调用
ticker = api.get_tick("BINGX___SPOT", "BTCUSDT")
balance = api.get_balance("BINGX___SPOT")
depth = api.get_depth("BINGX___SPOT", "BTCUSDT", count=20)
klines = api.get_kline("BINGX___SPOT", "BTCUSDT", period="1h", count=100)
```

---

## 架构

```
bt_api_bingx/
├── src/bt_api_bingx/
│   ├── __init__.py                  # 包入口
│   ├── plugin.py                    # register_plugin() — bt_api 插件入口点
│   ├── registry_registration.py      # register_bingx() — feeds / exchange_data 注册
│   ├── exchange_data/
│   │   └── __init__.py             # BingXExchangeData, BingXExchangeDataSpot
│   ├── feeds/
│   │   └── live_bingx/
│   │       ├── __init__.py
│   │       ├── request_base.py     # BingXRequestData 基类
│   │       └── spot.py             # BingXRequestDataSpot
│   └── errors/
│       └── __init__.py
├── tests/
├── docs/
└── pyproject.toml
```

---

## 支持的操作

| 类别 | 操作 | 说明 |
|---|---|---|
| **行情数据** | `get_ticker` | 24小时滚动行情 |
| | `get_depth` | 订单簿深度 |
| | `get_kline` | 周期: 1m/3m/5m/15m/30m/1h/2h/4h/6h/12h/1d/3d/1w/1M |
| | `get_exchange_info` | 交易所交易规则和交易对信息 |
| **账户** | `get_balance` | 所有资产余额 |
| | `get_account` | 完整账户信息 |
| **交易** | `make_order` | 限价单 |
| | `cancel_order` | 撤销单笔订单 |
| | `query_order` | 按ID查询订单 |
| | `get_open_orders` | 所有挂单 |

---

## 支持的 BingX 交易对

全部 BingX 现货交易对均支持，包括：

- **USDT 交易对**: `BTCUSDT`, `ETHUSDT`, `SOLUSDT`, `XRPUSDT`, `BNBUSDT` ...
- **USD 交易对**: `BTCUSD`, `ETHUSD`, `SOLUSD` ...
- **BTC 交易对**: `ETHBTC`, `BNBBTC` ...
- **ETH 交易对**: `BNBETH` ...
- **EUR 交易对**: `BTCEUR`, `ETHEUR` ...

---

## 限流配置

| 端点 | 限制 |
|---|---|
| 公开接口 | 200 请求/分钟 |
| 交易接口 | 100 请求/分钟 |

---

## 文档

| 文档 | 链接 |
|-----|------|
| **英文文档** | https://bt-api-bingx.readthedocs.io/ |
| **中文文档** | https://bt-api-bingx.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://cloudquant.github.io/bt_api_py/ |

---

## 许可证

MIT — 详见 [LICENSE](LICENSE)。

---

## 技术支持

- [GitHub Issues](https://github.com/cloudQuant/bt_api_bingx/issues) — bug 报告、功能请求
- 邮箱: yunjinqi@gmail.com