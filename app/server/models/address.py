from typing import Optional

from pydantic import BaseModel, Field


class AddressSchema(BaseModel):
    streetAddress: str = Field(...)
    city: str = Field(...)
    zip: str = Field(...)
    state: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "streetAddress": "1234 Main Drive",
                "city": "New York",
                "zip": "32123",
                "state": "NY"
            }
        }


class UpdateAddressModel(BaseModel):
    streetAddress: Optional[str]
    city: Optional[str]
    zip: Optional[str]
    state: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "streetAddress": "1234 Main Drive",
                "city": "New York",
                "zip": "32123",
                "state": "NY"
            }
        }
