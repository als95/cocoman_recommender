from pydantic import BaseModel


class ContentsBaseDto(BaseModel):
    id: int


class ContentsDto(BaseModel):
    title: str
    year: str
    country: str
    running_time: int
    grade_rate: str
    broadcaster: str
    open_date: str
    broadcast_date: str
    story: str
    poster_path: str


class ContentsUpdateDto(ContentsBaseDto, ContentsDto):
    pass
