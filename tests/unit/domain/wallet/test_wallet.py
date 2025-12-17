from uuid import uuid4
from decimal import Decimal
import pytest

from app.domain.wallet.entities import Wallet
from app.domain.shared.value_objects import Money
from app.domain.wallet.exceptions import InsufficientFundsError


def test_wallet_deposit():
    wallet = Wallet(wallet_id=uuid4(), user_id=uuid4())
    money = Money(amount=Decimal("100.00"), asset="BTC")
    wallet.deposit(money)
    assert wallet.balance_of("BTC") == Decimal("100.00")


def test_wallet_withdraw():
    wallet = Wallet(wallet_id=uuid4(), user_id=uuid4())
    money_deposit = Money(amount=Decimal("100.00"), asset="BTC")
    wallet.deposit(money_deposit)

    money_withdraw = Money(amount=Decimal("40.00"), asset="BTC")
    wallet.withdraw(money_withdraw)
    assert wallet.balance_of("BTC") == Decimal("60.00")


def test_wallet_cannot_withdraw_more_than_balance():
    wallet = Wallet(wallet_id=uuid4(), user_id=uuid4())
    money_deposit = Money(amount=Decimal("50.00"), asset="ETH")
    wallet.deposit(money_deposit)

    money_withdraw = Money(amount=Decimal("60.00"), asset="ETH")
    with pytest.raises(
        InsufficientFundsError, match="Insufficient funds for asset ETH"
    ):
        wallet.withdraw(money_withdraw)
