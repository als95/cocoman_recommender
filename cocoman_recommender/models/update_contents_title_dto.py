from pydantic import BaseModel

class UpdateContentsTitleDto(BaseModel):
    id: int
    title: str
