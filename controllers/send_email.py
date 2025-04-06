# FastApi
from fastapi    import status, APIRouter, Body

# Dtos
from dtos.email_dto import SendEmail

# Brevo
from services.my_brevo  import generate_email

# Templates
from templates.recover_password import recover_password

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
    generate_email(
        name        = send.name,
        email_from  = send.email_from,
        subject     = send.subject,
        emails      = send.emails,
        html        = recover_password(
            app_name        = send.name,
            user_name       = send.name,
            reset_url       = send.html,
            app_logo_url    = send.html
        )
    )

    return "Email sent successfully"