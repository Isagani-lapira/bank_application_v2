class BankDomain:
    def __init__(self,account_number:str=None,first_name:str=None,last_name:str=None,status:str=None,balance:float=None) -> None:
        self.__account_number = account_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__status = status
        self.__balance = balance

    
    # account number
    @property
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self,acc_number:str):
        self.__account_number = acc_number

    # first name
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self,fname:str):
        self.__first_name = fname

    # last name
    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self,lname:str):
        self.__last_name = lname

    # status
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self,status:str):
        self.__status = status

    # balance
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,balance:float):
        self.__balance = balance