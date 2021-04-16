from typing import List

from cocoman_recommender.models.actor_dto import ActorDto
from cocoman_recommender.schemas.actor import ActorRepository, Actor


class ActorService:
    def __init__(self, actor_repository: ActorRepository):
        self.actor_repository = actor_repository

    def find_all(self) -> List[ActorDto]:
        return self.actor_repository.get_all()

    def find_by_id(self, id: int) -> Actor:
        return self.actor_repository.get_by_id(id)

    def create(self, name: str, image_path: str):
        actor = Actor(name = name,
                      image_path = image_path
                      )
        self.actor_repository.create(actor)

    def delete_by_id(self, id: int):
        self.actor_repository.delete_by_id(id)

    def update(self, id: int, name: str, image_path: str):
        actor = Actor(name=name,
                      image_path=image_path
                      )
        self.actor_repository.update(id, actor)


