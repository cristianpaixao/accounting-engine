from decimal import Decimal
import pytest

from app.domain.shared.value_objects import Money


def test_money_creation():
    money = Money(amount=Decimal("100.00"), asset="BTC")
    assert money.amount == Decimal("100.00")
    assert money.asset == "BTC"


def test_money_must_be_positive():
    with pytest.raises(ValueError, match="Amount must be positive"):
        Money(amount=Decimal("0"), asset="BTC")


def test_money_must_have_asset():
    with pytest.raises(ValueError, match="Asset must be defined"):
        Money(amount=Decimal("100.00"), asset="")
