from typing import Union
from fastapi import FastAPI
from controllers import routes
from configuration import create_database


app = FastAPI()

# create_database()

app.include_router(routes)