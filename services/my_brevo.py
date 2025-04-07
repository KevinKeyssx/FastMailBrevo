# Future
from __future__ import print_function

# Brevo
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

# Utils
from pprint import pprint
from typing import List

# FastAPI
from fastapi import HTTPException

# Env
from os     import getenv
from dotenv import load_dotenv

# Dtos
from dtos.email_dto import EmailTo

# Load env
load_dotenv( dotenv_path = '.env' )
BREVO_API_KEY   = getenv( "BREVO_API_KEY" )
EMAIL_FROM_LIST = getenv( "EMAIL_FROM_LIST" ).split( "," )

# Instantiate the client
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = BREVO_API_KEY
api_instance = sib_api_v3_sdk.TransactionalEmailsApi( sib_api_v3_sdk.ApiClient( configuration ))


def validateEmails( email: str ) -> bool: return email in EMAIL_FROM_LIST


def generate_email(
    name        : str,
    email_from  : str,
    subject     : str,
    emailsTo    : List[EmailTo],
    html        : str
):
    if not validateEmails( email_from ):
        raise HTTPException(
            status_code = 404,
            detail      = "Email not found",
            headers     = {"X-Error": "Not found"},
        )

    sender  = { "name": name, "email": email_from }
    to      = [{ "email": email.email, "name": email.name } for email in emailsTo ]

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        sender          = sender,
        to              = to,
        subject         = subject,
        html_content    = html
    )

    try:
        api_response = api_instance.send_transac_email( send_smtp_email )
        pprint( api_response )
        print( "¡Correo enviado con éxito!" )
    except ApiException as e:
        print( f"Error al enviar el correo: {e}" )
