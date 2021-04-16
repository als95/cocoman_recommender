from fastapi import Depends, UploadFile, File
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from dependency_injector.wiring import inject, Provide

from cocoman_recommender.models.actor_dto import ActorDto
from cocoman_recommender.services.acter_service import ActorService
from cocoman_recommender.containers import Container

router = InferringRouter(prefix='/actor')

@cbv(router)
class ActorController:
    @inject
    def __init__(self, actor_service: ActorService = Depends(Provide[Container.actor_service])):
        self.actor_service = actor_service

    @router.post('/all')
    async def get_all(self):
        return self.actor_service.find_all()

    @router.post('/{id}')
    async def get_by_id(self, id: int):
        return self.actor_service.find_by_id(id)

    @router.post('/create')
    async def create(self, actor_dto: ActorDto):
        actor_dto.name = '아이유'
        actor_dto.image_path = "C://Users//bjw//Desktop//BAE//IU.jpg"
        return self.actor_service.create(actor_dto.name, actor_dto.image_path)

    @router.post('/delete')
    async def delete(self, id: int):
        return self.actor_service.delete_by_id()
    @router.post('/update/{id}')
    async def update(self, id: int, actor_dto: ActorDto):
        actor_dto.name = '서예지'
        actor_dto.image_path = "C://Users//bjw//Desktop//BAE//SEO.jpg"
        return self.actor_service.update(id, actor_dto.name, actor_dto.image_path)
