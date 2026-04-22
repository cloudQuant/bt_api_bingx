from bt_api_base.error import ErrorTranslator, UnifiedErrorCode


class BingXErrorTranslator(ErrorTranslator):
    ERROR_MAP = {
        "10001": (UnifiedErrorCode.INVALID_API_KEY, "Invalid API key"),
        "10002": (UnifiedErrorCode.INVALID_SIGNATURE, "Signature verification failed"),
        "10003": (UnifiedErrorCode.RATE_LIMIT_EXCEEDED, "Request rate limit exceeded"),
        "10004": (UnifiedErrorCode.INVALID_PARAMETER, "Invalid parameter"),
        "10005": (UnifiedErrorCode.PERMISSION_DENIED, "No permission for this operation"),
        "10006": (UnifiedErrorCode.INSUFFICIENT_BALANCE, "Insufficient balance"),
        "10007": (UnifiedErrorCode.INVALID_PRICE, "Invalid price"),
        "10008": (UnifiedErrorCode.MIN_NOTIONAL, "Order amount too small"),
        "10009": (UnifiedErrorCode.ORDER_NOT_FOUND, "Order does not exist"),
        "10010": (UnifiedErrorCode.MARKET_CLOSED, "Market is closed"),
        "10011": (UnifiedErrorCode.EXCHANGE_OVERLOADED, "Exchange is overloaded"),
        "10012": (UnifiedErrorCode.INTERNAL_ERROR, "Internal server error"),
    }


__all__ = ["BingXErrorTranslator"]
