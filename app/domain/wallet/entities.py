from uuid import UUID
from decimal import Decimal

from app.domain.shared.value_objects import Money
from app.domain.wallet.exceptions import InsufficientFundsError


class Wallet:
    def __init__(self, wallet_id: UUID, user_id: UUID):
        self.wallet_id = wallet_id
        self.user_id = user_id
        self._balances: dict[str, Decimal] = {}

    def deposit(self, money: Money) -> None:
        current = self._balances.get(money.asset, Decimal("0"))
        self._balances[money.asset] = current + money.amount

    def withdraw(self, money: Money) -> None:
        current = self._balances.get(money.asset, Decimal("0"))

        if current < money.amount:
            raise InsufficientFundsError(f"Insufficient funds for asset {money.asset}")

        self._balances[money.asset] = current - money.amount

    def balance_of(self, asset: str) -> Decimal:
        return self._balances.get(asset, Decimal("0"))
