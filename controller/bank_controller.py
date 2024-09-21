
from bll.bank_bll import BankBll
from domain.api_domain.bank_api_domain import BankAPIDomain
from domain.dto.bank_status_dto import BankStatusDTO


class BankController:
    
    def __init__(self) -> None:
        self.bank_bll = BankBll()
    
    def add_new_user(self, bank:BankAPIDomain):
        return self.bank_bll.create_user(bank)
    
    def update_acc_status(self,bank:BankStatusDTO):
        return self.bank_bll.update_account_status(bank.account_number,bank.status)