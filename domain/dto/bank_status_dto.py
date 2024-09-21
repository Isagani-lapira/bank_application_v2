from pydantic import BaseModel,Field

from domain.api_domain.bank_api_domain import StatusEnum


class BankStatusDTO(BaseModel):
    account_number:str = Field(default="",min_length=12,max_length=12)
    status:StatusEnum = Field(default="",description="Status only allowed Activated/Deactivated")