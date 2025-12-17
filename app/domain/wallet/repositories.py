from abc import ABC, abstractmethod


class WalletRepository(ABC):
    @abstractmethod
    def get_wallet_by_user_id(self, user_id):
        pass

    @abstractmethod
    def save_wallet(self, wallet):
        pass
