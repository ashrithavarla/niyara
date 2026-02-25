from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


# Equivalent to ContactFormDTO.java
class ContactFormDTO(BaseModel):
    name: str
    email: EmailStr
    contact_number: Optional[str] = None
    city: Optional[str] = None
    reason: str
    message: str
    recipient_email: EmailStr

    @field_validator("name", "reason", "message")
    @classmethod
    def not_blank(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Field must not be blank")
        return v
