from bll.bank_history_bll import BankHistoryBll
from domain.api_domain.transaction_api_domain import TransactionDomain


class BankHistoryController:

    def __init__(self) -> None:
        self.history_bll = BankHistoryBll()

    def get_account_bank_transaction(self,account_number:str):
        return self.history_bll.get_user_bank_history(account_number)
    
    def create_new_transaction(self,transaction:TransactionDomain):
        return self.history_bll.add_new_transaction(transaction)