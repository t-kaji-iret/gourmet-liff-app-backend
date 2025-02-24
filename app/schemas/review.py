from typing import Optional
from pydantic import BaseModel


class ReviewCreateResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ReviewCreate(BaseModel):
    name: str
    nearest_station: str
    genres: Optional[list[int]] = None
    website_url: Optional[str] = None
    comment: str
