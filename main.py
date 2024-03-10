from fastapi import FastAPI
from enum import Enum
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class LogLevel(str, Enum):
    INFO = "INFO"
    DEBUG = "DEBUG"
    ERROR = "ERROR"
    FATAL = "FATAL"

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

app = FastAPI()

def log_message(level: LogLevel, message: str):
    if LogLevel[level] >= LogLevel[LOG_LEVEL]:
        print(f"{datetime.utcnow().isoformat()} {level.lower()}: {message}")

@app.get("/info")
def get_info():
    log_message("INFO", "This is an info message")
    return {"message": "Info logged"}

@app.get("/debug")
def get_debug():
    log_message("DEBUG", "This is a debug message")
    return {"message": "Debug logged"}

@app.get("/error")
def get_error():
    log_message("ERROR", "This is an error message")
    return {"message": "Error logged"}

@app.get("/fatal")
def get_fatal():
    log_message("FATAL", "This is a fatal message")
    return {"message": "Fatal logged"}
