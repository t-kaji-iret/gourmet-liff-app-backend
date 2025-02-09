from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/hello-world", status_code=200)
def read_root():
    return {"message": "Hello SAM World"}


lambda_handler = Mangum(app)
