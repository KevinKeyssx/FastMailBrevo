from datetime import datetime

def create_base_template(
    app_name        : str,
    user_name       : str,
    redirect_url    : str,
    logo_url        : str,
    color           : str = None,
    text_color      : str = None,
    title           : str = "",
    content_title   : str = "",
    highlight_text  : str = "",
    button_text     : str = "",
    footer_year     : int = datetime.now().year,
    additional_content : str = ""
) -> str:
    """
    Creates a base email template with customizable content.
    
    Args:
        app_name: Name of the application
        user_name: Name of the user
        redirect_url: URL for the action button
        logo_url: URL for the logo image
        color: Primary color (optional)
        text_color: Text color (optional)
        title: Page title
        content_title: Title for the content section
        highlight_text: Text to be highlighted
        button_text: Text for the action button
        footer_year: Year for the footer copyright
        additional_content: Any additional HTML content to include
        
    Returns:
        str: Complete HTML template
    """
    # Set default colors if not provided
    if not color:
        gradient = '#6e8efb, #a777e3'
        highlight_border = '#a777e3'
    else:
        gradient = f'{color}, {color}'
        highlight_border = color

    if not text_color:
        text_color_header = '#ffffff'
        button_text_color = '#ffffff'
    else:
        text_color_header = text_color
        button_text_color = text_color

    # Define common colors
    bg_color = '#f7f7f7'
    primary_color = f'linear-gradient(135deg, {gradient})'
    heading_color = '#2c3e50'
    button_color = f'linear-gradient(135deg, {gradient})'
    highlight_bg = '#f8f4ff'
    muted_text_color = '#777777'

    return f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
            <style>
                body {{
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                    background-color: {bg_color};
                    margin: 0;
                    padding: 0;
                    color: #333;
                    line-height: 1.6;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                }}
                .header {{
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background: {primary_color};
                    padding: 10px 0px 10px 30px;
                    color: {text_color_header};
                }}
                .logo {{
                    max-width: 60px;
                    max-height: 60px;
                    margin-top: 7px;
                    margin-right: 10px;
                }}
                .content {{
                    padding: 30px;
                }}
                h1 {{
                    color: {heading_color};
                }}
                .button {{
                    display: inline-block;
                    padding: 12px 30px;
                    background: {button_color};
                    color: {button_text_color} !important;
                    text-decoration: none;
                    border-radius: 30px;
                    font-weight: bold;
                    margin: 20px 0;
                }}
                .footer {{
                    text-align: center;
                    padding: 20px;
                    background: #f5f5f5;
                    color: #777;
                    font-size: 12px;
                }}
                .highlight {{
                    background-color: {highlight_bg};
                    padding: 15px;
                    border-radius: 5px;
                    margin: 20px 0;
                    border-left: 4px solid {highlight_border};
                }}
                .text-muted {{
                    color: {muted_text_color};
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <img src="{logo_url}" alt="{app_name}" class="logo">
                    <h1>{app_name}</h1>
                </div>

                <div class="content">
                    <h2>Hola {user_name},</h2>

                    {content_title}

                    <div class="highlight">
                        <p>{highlight_text}</p>
                    </div>

                    <a href="{redirect_url}" class="button">{button_text}</a>

                    <p class="text-muted">O copia y pega este enlace en tu navegador:</p>

                    <p style="word-break: break-all;"><a href="{redirect_url}">{redirect_url}</a></p>

                    <p>Este enlace expirará en 1 hora por seguridad.</p>

                    {additional_content}
                </div>

                <div class="footer">
                    <p>© {footer_year} {app_name}. Todos los derechos reservados.</p>
                    <p>Si tienes problemas con el botón, copia y pega la URL en tu navegador.</p>
                </div>
            </div>
        </body>
    </html>"""
