from uuid import UUID


class Wallet:
    def __init__(self, wallet_id: UUID, user_id: UUID):
        self.wallet_id = wallet_id
        self.user_id = user_id
