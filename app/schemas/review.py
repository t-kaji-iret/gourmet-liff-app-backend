from typing import Optional
from pydantic import BaseModel


class ReviewCreateResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ReviewCreateRequest(BaseModel):
    restaurant_name: str
    nearest_station: str
    genres: Optional[list[int]] = None
    url: Optional[str] = None
    comment: str
