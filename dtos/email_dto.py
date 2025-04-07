from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr, Field

from enum import Enum


class TemplateType( Enum ):
    RECOVER_PASSWORD    = "recover_password"
    VERIFY_ACCOUNT      = "verify_account"


class Template( BaseModel ):
    type: TemplateType = Field(
        ...,
        example = TemplateType.RECOVER_PASSWORD
    )
    redirect_url: Optional[str] = Field(
        None,
        min_length=12,
        max_length=255,
        example = "https://example.com/reset-password"
    )
    logo_url: Optional[str] = Field(
        None,
        min_length=12,
        max_length=255,
        example = "https://example.com/logo.png"
    )
    color: Optional[str] = Field(
        None,
        min_length=7,
        max_length=7,
        example = "#000000"
    )
    text_color: Optional[str] = Field(
        None,
        min_length=7,
        max_length=7,
        example = "#ffffff"
    )

    def __str__(self) -> str:
        return self.name.lower()


class EmailTo( BaseModel ):
    email: EmailStr = Field(
        ...,
        example = "john@example.com"
    )
    name: str = Field(
        None,
        min_length=3,
        max_length=100,
        example = "John Doe"
    )


class SendEmail( BaseModel ):
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        example="GuardianAPI"
    )
    email_from: str = Field(
        ...,
        example="smart.new.gen.official@sng.com"
    )
    subject: Optional[str] = Field(
        None,
        min_length=5,
        max_length=100,
        example = "Título del correo electrónico"
    )
    emailsTo: List[EmailTo] = Field(
        ...,
        min_items=1,
        example = [{"email": "john@example.com", "name": "John Doe"}]
    )
    template: Union[Template, str] = Field(
        ...,
        description = "Puede ser un objeto Template estructurado o HTML raw como string"
    )
