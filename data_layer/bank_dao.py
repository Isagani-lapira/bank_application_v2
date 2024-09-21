
from data_layer.abstract_dao import AbstractBankDao
from domain.bank_domain import BankDomain


class BankDao(AbstractBankDao):

    def get_file_name(self):
        return 'bank_details.json'
    
    def get_all_account_details(self):
        result = []
        for account_number,details in self.load_file_data().items():
            fname = details.get('name').get('first_name')
            lname = details.get('name').get('last_name')
            status = details.get('status')
            balance = details.get('balance')
            result.append(BankDomain(account_number,fname,lname,status,balance))

        return result
    
    def add_account(self,data:dict):
        self._insert_new_data(data)

    def update_account(self,data:dict):
        self._insert_new_data(data)