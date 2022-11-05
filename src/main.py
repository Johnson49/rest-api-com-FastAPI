from typing import Union
from fastapi import FastAPI
from controllers import routes

app = FastAPI()

app.include_router(routes)