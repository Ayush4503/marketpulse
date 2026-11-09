import pytest

from marketpulse.asset import Asset, AssetType


def test_asset_normalizes_ticker():
    asset = Asset(
        ticker="  aapl  ",
        name="Apple Inc.",
        asset_type=AssetType.STOCK,
        exchange="NASDAQ",
        currency="USD",
    )

    assert asset.ticker == "AAPL"


def test_asset_rejects_empty_ticker():
    with pytest.raises(ValueError):
        Asset(
            ticker="",
            name="Apple Inc.",
            asset_type=AssetType.STOCK,
            exchange="NASDAQ",
            currency="USD",
        )


def test_asset_rejects_whitespace_only_ticker():
    with pytest.raises(ValueError):
        Asset(
            ticker="      ",
            name="Apple Inc.",
            asset_type=AssetType.STOCK,
            exchange="NASDAQ",
            currency="USD",
        )


def test_asset_rejects_unsupported_asset_type():
    with pytest.raises(ValueError):
        Asset(
            ticker="TEST",
            name="Test Asset",
            asset_type="BANANA",
            exchange="TEST",
            currency="USD",
        )


@pytest.mark.parametrize(
    "asset_type",
    [
        AssetType.STOCK,
        AssetType.ETF,
        AssetType.CRYPTO,
        AssetType.FUTURE,
        AssetType.OPTION,
    ],
)
def test_asset_accepts_supported_asset_type(asset_type):
    asset = Asset(
        ticker="TEST",
        name="Test Asset",
        asset_type=asset_type,
        exchange="TEST",
        currency="USD",
    )

    assert asset.asset_type == asset_type