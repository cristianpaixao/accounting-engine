from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Money:
    amount: Decimal
    asset: str

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount must be positive")

        if not self.asset:
            raise ValueError("Asset must be defined")
