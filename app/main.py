from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from mangum import Mangum
from exception.exceptions import NotFoundException
from routers.review_router import router as review_router
from schemas.error import ErrorResponse
from aws_lambda_powertools import Logger

app = FastAPI()
logger = Logger()


# バリデーションエラー時のハンドリング
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error("occurred validation error", exc.errors())
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(message="入力内容に不備があります。").dict()
    )


# リソースが存在しないエラー時のハンドリング
@app.exception_handler(NotFoundException)
def validation_exception_handler(request: Request, exc: NotFoundException):
    logger.error("not found exception", exc)
    return JSONResponse(
        status_code=404,
        content=ErrorResponse(message=exc.message).dict()
    )


# その他エラー時のハンドリング
@app.exception_handler(Exception)
def exception_handler(request: Request, exc: Exception):
    logger.error("occurred unexpected error", exc)
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(message="予期せぬエラーが発生しました。").dict()
    )


# ルーティング
app.include_router(review_router, prefix="/review", tags=["review"])

lambda_handler = Mangum(app)
