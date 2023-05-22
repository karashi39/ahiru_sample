import os

from fastapi import FastAPI


GREETING = os.getenv("GREETING", default="World")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"Hello {GREETING}"}
