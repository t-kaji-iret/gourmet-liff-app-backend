from sqlalchemy.orm import Session

from exception.exceptions import NotFoundException
from models.genre import Genre
from models.restaurant_genre import RestaurantGenre
from models.review import Review
from models.user import User
from schemas.review import ReviewCreateRequest


def create(
        review_request: ReviewCreateRequest,
        user: User,
        session: Session
) -> Review:
    genres = session.query(Genre).filter(Genre.id.in_(review_request.genres)).all()
    if len(genres) != len(review_request.genres):
        raise NotFoundException("存在しないジャンルです。")

    review = Review(
        user_id=user.id,
        restaurant_name=review_request.restaurant_name,
        nearest_station=review_request.nearest_station,
        comment=review_request.comment,
        url=review_request.url
    )
    session.add(review)
    session.flush()

    restaurant_genres = []
    for genre in genres:
        restaurant_genre = RestaurantGenre(
            review_id=review.id,
            genre_id=genre.id
        )
        restaurant_genres.append(restaurant_genre)
    session.add_all(restaurant_genres)

    session.commit()
    return review
