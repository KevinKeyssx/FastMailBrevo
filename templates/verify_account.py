from datetime import datetime

def verify_account(
    app_name        : str,
    user_name       : str,
    user_email      : str,
    redirect_url    : str,
    logo_url        : str,
    color           : str or None,
    text_color      : str or None,
) -> str:
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
            <title>Verifica tu cuenta</title>
            <style>
                body {{
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                    background-color: {bg_color};
                    margin: 0;
                    padding: 0;
                    color: {text_color_header};
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
                    color: #ffffff;
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
                    <img src="{ logo_url }" alt="{ app_name }" class="logo">
                    <h1>{ app_name }</h1>
                </div>

                <div class="content">
                    <h2>Hola { user_name },</h2>

                    <p>Gracias por registrarte en <strong>{ app_name }</strong>.</p>

                    <div class="highlight">
                        <p>Por favor verifica tu dirección de correo electrónico (<strong>{ user_email }</strong>) para activar tu cuenta.</p>
                    </div>

                    <p>Haz clic en el botón para completar la verificación:</p>

                    <a href="{ redirect_url }" class="button">Verificar mi cuenta</a>

                    <p class="text-muted">O copia y pega este enlace en tu navegador:</p>

                    <p style="word-break: break-all;"><a href="{ redirect_url }">{ redirect_url }</a></p>

                    <p>Este enlace expirará en 24 horas por seguridad.</p>

                    <p>Si no creaste una cuenta con nosotros, ignora este mensaje.</p>

                    <p>¡Bienvenido a { app_name }!</p>

                    <p>El equipo de { app_name }</p>
                </div>

                <div class="footer">
                    <p>© { datetime.now().year } { app_name }. Todos los derechos reservados.</p>
                    <p>Si tienes problemas con el botón, copia y pega la URL en tu navegador.</p>
                </div>
            </div>
        </body>
    </html>"""