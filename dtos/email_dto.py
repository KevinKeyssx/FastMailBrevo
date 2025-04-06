from typing import List
from pydantic import BaseModel, EmailStr, Field


class SendEmail( BaseModel ):
    name: str = Field(
        ...,
        example="GuardianAPI"
    )
    email_from: str = Field(
        ...,
        example="smart.new.gen.official@sng.com"
    )
    subject: str = Field(
        ...,
        example = "Título del correo electrónico"
    )
    emails: List[EmailStr] = Field(
        ...,
        example = ["john@example.com"]
    )
    html: str = Field(
        ...,
        example = "<h1>Se envió correctamente</h1>"
    )
