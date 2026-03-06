import os
import webbrowser
import time

webbrowser.open("http://127.0.0.1:8000/dashboard")
os.system("uvicorn app.main:app --reload")