from templates.base_template import create_base_template

def verify_account(
    app_name        : str,
    user_name       : str,
    user_email      : str,
    redirect_url    : str,
    logo_url        : str,
    color           : str = None,
    text_color      : str = None,
) -> str:
    """
    Creates a verification email template.
    
    Args:
        app_name: Name of the application
        user_name: Name of the user
        user_email: Email of the user
        redirect_url: URL for the verification
        logo_url: URL for the logo image
        color: Primary color (optional)
        text_color: Text color (optional)
        
    Returns:
        str: Complete HTML template for account verification
    """
    content_title = f"<p>Gracias por registrarte en <strong>{app_name}</strong>.</p>"
    
    highlight_text = f"Por favor verifica tu dirección de correo electrónico (<strong>{user_email}</strong>) para activar tu cuenta."
    
    additional_content = f"""
    <p>Si no creaste una cuenta con nosotros, ignora este mensaje.</p>
    <p>¡Bienvenido a {app_name}!</p>
    """
    
    return create_base_template(
        app_name=app_name,
        user_name=user_name,
        redirect_url=redirect_url,
        logo_url=logo_url,
        color=color,
        text_color=text_color,
        title="Verifica tu cuenta",
        content_title=content_title,
        highlight_text=highlight_text,
        button_text="Verificar mi cuenta",
        additional_content=additional_content
    )