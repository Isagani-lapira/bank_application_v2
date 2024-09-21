
from data_layer.bank_dao import BankDao
from domain.api_domain.bank_api_domain import BankAPIDomain
from domain.bank_domain import BankDomain


class BankBll:
    def __init__(self) -> None:
        self.bank_dao = BankDao()

    def create_user(self,bank):
        new_data = {
            bank.account_number:{
                "name":{
                    "first_name":bank.first_name,
                    "last_name":bank.last_name
                },
                "status":bank.status,
                "balance":bank.balance
            }
        }
        self.bank_dao.add_account(new_data)

    def update_account_status(self,acc_number:str,status:str):
        data = self.find_user(acc_number)
        data.status = status
        self.create_user(data)


    def find_user(self,acc_number:str)->BankDomain:
        for accounts in self.bank_dao.get_all_account_details():
            if accounts.account_number == acc_number:
                return accounts
            
        return None
    
    def get_account_balance(self,acc_number:str)->float:
        return self.find_user(acc_number).balance
    
    def update_account_balance(self,acc_number:str,deducted_money:float)->float:
        current_bal = self.find_user(acc_number).balance
        updated_bal = current_bal-deducted_money
        data = self.find_user(acc_number)
        data.balance = updated_bal
        self.create_user(data)

        return data.balance