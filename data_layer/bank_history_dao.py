
from data_layer.abstract_dao import AbstractBankDao
from domain.bank_history_domain import BankHistoryDomain


class BankHistoryDao(AbstractBankDao):

    def get_transaction_details(self):
        results = []
        for details in self.load_file_data().values():
            account_number = details.get('account_number')
            date = details.get('date')
            description = details.get('description')
            credit = details.get('credit')
            debit = details.get('debit')
            deducted_money = details.get('deducted_money')
            balance = details.get('balance')
            results.append(BankHistoryDomain(account_number,date,description,credit,debit,deducted_money,balance))

        return results   
    
    def add_new_transaction(self,data:dict):
        self._insert_new_data(data)


    def find_by_account_number(self,account_number)->list:
        results = []
        for transaction in self.get_transaction_details():
            if transaction.account_number == account_number:
                results.append(transaction.to_dict())

        return results
    

    def get_file_name(self):
        return 'bank_transac_data.json'