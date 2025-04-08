from templates.base_template import create_base_template

def recover_password(
    app_name        : str,
    user_name       : str,
    redirect_url    : str,
    app_logo_url    : str,
    color           : str = None,
    text_color      : str = None
) -> str:
    """
    Creates a password recovery email template.
    
    Args:
        app_name: Name of the application
        user_name: Name of the user
        redirect_url: URL for the password reset
        app_logo_url: URL for the logo image
        color: Primary color (optional)
        text_color: Text color (optional)
        
    Returns:
        str: Complete HTML template for password recovery
    """
    content_title = f"<p>Recibimos una solicitud para restablecer la contraseña de tu cuenta en <strong>{app_name}</strong>.</p>"

    highlight_text = f"Por favor restablece tu contraseña para continuar usando <strong>{app_name}.</strong>"

    additional_content = f"""
    <p>Si no solicitaste este cambio, puedes ignorar este mensaje.</p>
    <p>¡Gracias por usar {app_name}!</p>
    """

    return create_base_template(
        app_name            = app_name,
        user_name           = user_name,
        redirect_url        = redirect_url,
        logo_url            = app_logo_url,
        color               = color,
        text_color          = text_color,
        title               = "Recupera tu contraseña",
        content_title       = content_title,
        highlight_text      = highlight_text,
        button_text         = "Restablecer contraseña",
        additional_content  = additional_content
    )