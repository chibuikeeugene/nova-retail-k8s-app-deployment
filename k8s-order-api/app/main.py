import os
from fastapi import FastAPI
from socket import gethostname

#creating a fastapi object
app = FastAPI()

# load environment variables
APP_ENV = os.getenv("APP_ENV", "dev")
APP_VERSION = os.getenv("APP_VERSION", "2.0.0")

#TODO 1: create status endpoint
@app.get("/")
def root():
    """get application state status"""
    return {
        "service":"order-api",
        "environment": APP_ENV,
        "version":APP_VERSION,
        "pod": gethostname()
    }


#TODO 2: create health endpoint
@app.get("/health")
def health():
    """get application health status"""
    return {
        "status": "healthy"
    }


#TODO 3: create order endpoint
@app.get("/orders")
def orders():
    """get customer order"""
    return {
        "orders" : [
            {"id":1001, "product":"gameboard", "status":"processed"},
            {"id":1002, "product":"book", "status":"pending"}
        ]
    }