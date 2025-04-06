# FastApi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes
from controllers.send_email import send_email

# FastApi
app = FastAPI(
    title       = 'FastMailBrevo',
    description = 'Send any email to any email address with brevo and fastapi',
)

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins       = ["*"],
    allow_credentials   = True,
    allow_methods       = ["*"],
    allow_headers       = ["*"],
)

# Versions
VERSION = "/v1"
API     = VERSION + "/api"

# Includes
app.include_router( send_email, prefix=API )