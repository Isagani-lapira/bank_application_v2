from pydantic import BaseModel,Field
from enum import Enum
class StatusEnum(str,Enum):
    activated = 'Activated'
    deactivated = 'Deactivated'

class BankAPIDomain(BaseModel):
    account_number:str = Field(default="",min_length=12,max_length=12)
    first_name:str = Field(default="")
    last_name:str = Field(default="")
    status:StatusEnum = Field(default="",description="Status only allowed Activated/Deactivated")
    balance:float = Field(default=0.0)