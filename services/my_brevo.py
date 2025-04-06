from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from typing import List

# Env
from os     import getenv
from dotenv import load_dotenv

# Load env
load_dotenv( dotenv_path = '.env' )
BREVO_API_KEY    = getenv( "BREVO_API_KEY" )

# Instantiate the client
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = BREVO_API_KEY
api_instance = sib_api_v3_sdk.TransactionalEmailsApi( sib_api_v3_sdk.ApiClient( configuration ))


def generate_email(
    name        : str,
    email_from  : str,
    subject     : str,
    emails      : List[str],
    html        : str
):
    sender  = { "name": name, "email": email_from }
    to      = [{ "email": email } for email in emails ]

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
