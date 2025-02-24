from sqlalchemy.orm import Session
from orm.models.review import Review
from schemas.review import ReviewCreate


def create_review(session: Session, review: ReviewCreate) -> Review:
    with session:
        review = Review(**review.dict())
        session.add(review)
        session.refresh(review)
        return review
