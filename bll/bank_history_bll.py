

from bll.bank_bll import BankBll
from data_layer.bank_history_dao import BankHistoryDao
from domain.api_domain.transaction_api_domain import PaymentCard, TransactionDomain


class BankHistoryBll:

    def __init__(self) -> None:
        self.__bank_dao = BankHistoryDao()
        self.__bank_bll = BankBll()

    def get_user_bank_history(self,account_number)->list:
        return self.__bank_dao.find_by_account_number(account_number)
    

    def add_new_transaction(self,transaction_details:TransactionDomain):

        if self.__is_balance_still_valid(transaction_details.account_number,transaction_details.deducted_money):
            # update the balance and get the new updated balance
            updated_balance = self.__bank_bll.update_account_balance(transaction_details.account_number,transaction_details.deducted_money)
            is_credit = self.__is_credit(transaction_details.card.value)
            new_transac = {
                transaction_details.transaction_id: {
                    "account_number":transaction_details.account_number,
                    "date":transaction_details.date,
                    "description":transaction_details.description,
                    "credit":is_credit,
                    "debit":not is_credit,
                    "deducted_money":transaction_details.deducted_money,
                    "balance":updated_balance
                }
            }
            return self.__bank_dao.add_new_transaction(new_transac)
        return "Current balance not satisfy the transaction"


    def __is_credit(self,card):
        return card == PaymentCard.credit.value
    
    def __is_balance_still_valid(self,account_number,deducted_money:float)->bool:
        current_balance = self.__bank_bll.get_account_balance(account_number)
        transaction_amount = current_balance-deducted_money

        if transaction_amount > 0:
            return True
        
        return False