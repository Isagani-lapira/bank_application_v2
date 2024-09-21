class BankHistoryDomain:

    def __init__(self,account_number:str,date:str,description:str,
                 credit:str,debit:str,deducted_money,balance:float) -> None:
        
        self.__account_number = account_number
        self.__date = date
        self.__description = description
        self.__credit = credit
        self.__debit = debit
        self.__deducted_money = deducted_money
        self.__balance = balance

    def to_dict(self):
        return {
            "account_number": self.__account_number,
            "date": self.__date,
            "description": self.__description,
            "credit": self.__credit,
            "debit": self.__debit,
            "balance": self.__balance,
        }

    # acc number
    @property
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self,acc_number):
        self.__account_number = acc_number

    # date
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self,date):
        self.__date = date

    
    # description
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self,descrip):
        self.__description = descrip


    # credit
    @property
    def credit(self):
        return self.__credit
    
    @credit.setter
    def credit(self,credit):
        self.__credit = credit

    # debit
    @property
    def debit(self):
        return self.__debit
    
    @debit.setter
    def debit(self,debit):
        self.__debit = debit


    # deducted money
    @property
    def deducted_money(self):
        return self.__deducted_money
    
    @deducted_money.setter
    def deducted_money(self,deducted_money):
        self.__deducted_money = deducted_money

    
    # balance
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,balance):
        self.__balance = balance