from datetime import datetime

def recover_password(
    app_name        : str,
    user_name       : str,
    reset_url       : str,
    app_logo_url    : str
) -> str:
    current_year = datetime.now().year
    return f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Recupera tu contraseña</title>
            <style>
                body {
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                    background-color: #f7f7f7;
                    margin: 0;
                    padding: 0;
                    color: #333;
                }
                .container {
                    max-width: 600px;
                    margin: 20px auto;
                    background: #ffffff;
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                }
                .header {
                    background: linear-gradient(135deg, #6e8efb, #a777e3);
                    padding: 30px;
                    text-align: center;
                    color: white;
                }
                .logo {
                    max-width: 150px;
                    margin-bottom: 20px;
                }
                .content {
                    padding: 30px;
                }
                h1 {
                    color: #2c3e50;
                    margin-top: 0;
                }
                .button {
                    display: inline-block;
                    padding: 12px 30px;
                    background: linear-gradient(135deg, #6e8efb, #a777e3);
                    color: white !important;
                    text-decoration: none;
                    border-radius: 30px;
                    font-weight: bold;
                    margin: 20px 0;
                }
                .footer {
                    text-align: center;
                    padding: 20px;
                    background: #f5f5f5;
                    color: #777;
                    font-size: 12px;
                }
                .highlight {
                    background-color: #f8f4ff;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 20px 0;
                    border-left: 4px solid #a777e3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <img src="{app_logo_url}" alt="Logo" class="logo">
                    <h1>{app_name}</h1>
                </div>

                <div class="content">
                    <h2>Hola {user_name},</h2>

                    <p>Recibimos una solicitud para restablecer la contraseña de tu cuenta en <strong>{app_name}</strong>.</p>

                    <div class="highlight">
                        <p>Si no solicitaste este cambio, puedes ignorar este mensaje.</p>
                    </div>

                    <p>Para crear una nueva contraseña, haz clic en el siguiente botón:</p>

                    <a href="{reset_url}" class="button">Restablecer contraseña</a>

                    <p>O copia y pega este enlace en tu navegador:</p>

                    <p style="word-break: break-all;"><a href="{reset_url}">{reset_url}</a></p>

                    <p>Este enlace expirará en 24 horas por seguridad.</p>

                    <p>¡Gracias por usar {app_name}!</p>

                    <p>El equipo de {app_name}</p>
                </div>

                <div class="footer">
                    <p>© {current_year} {app_name}. Todos los derechos reservados.</p>
                    <p>Si tienes problemas con el botón, copia y pega la URL en tu navegador.</p>
                </div>
            </div>
        </body>
        </html>"""