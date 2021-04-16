from pydantic import BaseModel


class ActorDto(BaseModel):
    id: str
    name: str
    image_path: str
