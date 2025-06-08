from enum import Enum
from pydantic import BaseModel, Field
from datetime import date
# define genre choices
class GenreUrlChoices(Enum):
    ROCK = "Rock"
    POP = "Pop"
    JAZZ = "Jazz"
    CLASSICAL = "Classical"
    HIP_HOP = "Hip Hop"

class Album(BaseModel):
    title: str = Field(..., description="The title of the album")
    release_date: date = Field(..., description="The date the album was released")

class Band(BaseModel):
    id: int = Field(..., description="The unique identifier for the band")
    name: str = Field(..., description="The name of the band")
    genre: GenreUrlChoices = Field(..., description="The genre of the band")
    albutms: list[Album] = []

