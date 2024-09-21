
from controller.bank_controller import BankController
from controller.bank_history_controller import BankHistoryController
from data_layer.bank_dao import BankDao
from domain.api_domain.bank_api_domain import BankAPIDomain, StatusEnum
from domain.api_domain.transaction_api_domain import TransactionDomain
from domain.bank_domain import BankDomain
from fastapi import FastAPI

from domain.dto.bank_status_dto import BankStatusDTO

api = FastAPI()
base_url = '/api'
controller =  BankController()
transac_history_controller = BankHistoryController()

@api.post(f'{base_url}/register')
def add_new_user(bank:BankAPIDomain):
    return controller.add_new_user(bank)


@api.put(f'{base_url}/status-update')
def update_acc_status(bank:BankStatusDTO):
    return controller.update_acc_status(bank)


@api.get(f'{base_url}/accounts/')
def get_transaction(account_number:str):
    return transac_history_controller.get_account_bank_transaction(account_number)


@api.post(f'{base_url}/transaction/add/credit')
def add_transaction(transaction:TransactionDomain):
    transac_history_controller.create_new_transaction(transaction)

