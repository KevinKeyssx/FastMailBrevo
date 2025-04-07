# FastApi
from fastapi    import status, APIRouter, Body, HTTPException

# Dtos
from dtos.email_dto import SendEmail

# Brevo
from services.my_brevo  import generate_email

# Templates
from templates.admin_template import admin_subject, admin_template

# Routes
send_email     = APIRouter()
tags            = "Send Email"

# Services
@send_email.post(
    path            = "/send",
    response_model  = str,
    status_code     = status.HTTP_200_OK,
    summary         = 'Send email',
    tags            = [ tags ]
)
async def send(
    send: SendEmail = Body(...)
):
    if isinstance( send.template, str ):
        html_content = send.template

        if not send.subject:
            raise HTTPException(
                status_code = 400,
                detail      = "Subject is required",
                headers     = {"X-Error": "Subject is required"},
            )

        subject = send.subject
    else:
        if len( send.emailsTo ) > 1:
            raise HTTPException(
                status_code = 400,
                detail      = "EmailTo must be a list of 1 element",
                headers     = {"X-Error": "EmailTo must be a list of 1 element"},
            )

        html_content    = admin_template( send )
        subject         = admin_subject( send.template )

    generate_email(
        name        = send.name,
        email_from  = send.email_from,
        subject     = subject,
        emailsTo    = send.emailsTo,
        html        = html_content
    )

    return "Email sent successfully"