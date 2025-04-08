from dtos.email_dto import SendEmail, Template, TemplateType

from templates.recover_password import recover_password
from templates.verify_account   import verify_account


def admin_template( send: SendEmail ) -> str:
    if send.template.type == TemplateType.RECOVER_PASSWORD:
        return recover_password(
            app_name        = send.name,
            user_name       = send.emailsTo[0].name,
            redirect_url    = send.template.redirect_url,
            app_logo_url    = send.template.logo_url,
            color           = send.template.color,
            text_color      = send.template.text_color,
        )
    elif send.template.type == TemplateType.VERIFY_ACCOUNT:
        return verify_account(
            app_name        = send.name,
            user_name       = send.emailsTo[0].name,
            user_email      = send.emailsTo[0].email,
            redirect_url    = send.template.redirect_url,
            logo_url        = send.template.logo_url,
            color           = send.template.color,
            text_color      = send.template.text_color,
        )
    else:
        return "Template not found"


def admin_subject( template: Template ) -> str:
    if template.type == TemplateType.RECOVER_PASSWORD:
        return 'Recuperar contraseña'
    elif template.type == TemplateType.VERIFY_ACCOUNT:
        return 'Verifica tu cuenta'
    else:
        return "Template not found"