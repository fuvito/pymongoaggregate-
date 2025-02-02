from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from app.server.models.address import AddressSchema


class StudentSchema(BaseModel):
    name: str = Field(None)
    email: EmailStr = Field(None)
    course_of_study: str = Field(None)
    grade: str = Field(None)
    year: int = Field(None, gt=0, lt=9)
    gpa: float = Field(None, le=4.0)
    address: AddressSchema = Field(None)

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources engineering",
                "grade": "A",
                "year": 2,
                "gpa": "3.0",
            }
        }


class UpdateStudentModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    grade: Optional[str]
    year: Optional[int]
    gpa: Optional[float]
    address: Optional[AddressSchema]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "grade": "A",
                "year": 4,
                "gpa": "4.0",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
