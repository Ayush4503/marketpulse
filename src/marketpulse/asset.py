from dataclasses import dataclass
from enum import Enum


class AssetType(Enum):
    STOCK = "STOCK"
    ETF = "ETF"
    CRYPTO = "CRYPTO"
    FUTURE = "FUTURE"
    OPTION = "OPTION"


@dataclass
class Asset:
    ticker: str
    name: str
    asset_type: AssetType
    exchange: str
    currency: str

    def __post_init__(self):
        self.ticker = self.ticker.strip().upper()

        if not self.ticker:
            raise ValueError("Ticker cannot be empty")

        if not isinstance(self.asset_type, AssetType):
            raise ValueError("Asset type not supported")