from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.auth import get_current_user
from database import session_factory
from models.user import User
from schemas.review import ReviewCreateRequest, ReviewCreateResponse
from usecases.review.create import create

router = APIRouter()


@router.post("/", response_model=ReviewCreateResponse)
def post_review(
        body: ReviewCreateRequest,
        user: User = Depends(get_current_user),
        session: Session = Depends(session_factory)
):
    new_review = create(body, user, session)
    return new_review
