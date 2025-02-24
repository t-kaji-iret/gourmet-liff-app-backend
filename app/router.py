from fastapi import FastAPI, Depends
from mangum import Mangum
from sqlalchemy.orm import Session
from orm.setting import session_factory
from cruds.review import create_review
from schemas.review import ReviewCreate, ReviewCreateResponse

app = FastAPI()


@app.get("/review", response_model=ReviewCreateResponse)
async def post_review(body: ReviewCreate, db: Session = Depends(session_factory)):
    return create_review(db, body)


lambda_handler = Mangum(app)
