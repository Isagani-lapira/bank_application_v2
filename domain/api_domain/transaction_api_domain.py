from pydantic import BaseModel,Field
from enum import Enum

class PaymentCard(str,Enum):
    credit = "Credit"
    debit = "Debit"


class TransactionDomain(BaseModel):
    transaction_id:str = Field(
        default="",
        min_length=6,
        max_length=10)
    
    account_number:str = Field(
        default="",
        min_length=12,
        max_length=12)
    
    date:str = Field(default="")
    description:str = Field(default="",max_length=60,description="transaction details")
    card:PaymentCard = Field(default="")
    deducted_money:float = Field(default=0.0)