import socket, json
   
import argparse

from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

import sys, os

  
from fastapi.middleware import BaseHTTPMiddleware

from customlog import log_middleware

# Swagger setup
app = FastAPI(    
    title="Example API",
    description='Just a simple example for the @guicarvalho Custom Log Middleware for FastAPI.',
    summary="Simple FastAPI example.",
    version="1.0.0",
    terms_of_service="https://fastapi.tiangolo.com/tutorial/metadata/",
    contact={
        "name": "Simple FastAPI example",
        "url": "https://fastapi.tiangolo.com/tutorial/metadata/",
        "email": "gerson.freire@gmail.com",
    },
    debug=False,
    openapi_url=f"/example.json",
    )

app.add_middleware(
    BaseHTTPMiddleware,
    dispatch=log_middleware
)

@app.get("/")
def read_root():
    return {"Status": "Online"}

# ------------------------------
# Run the server
if __name__ == "__main__":  

    uvicorn.run(
        app=app,
        host='0.0.0.0', 
        port=8888,
        )     
