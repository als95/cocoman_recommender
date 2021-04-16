from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from dependency_injector.wiring import inject, Provide

from cocoman_recommender.models.contents_dto import ContentsDto, ContentsUpdateDto
from cocoman_recommender.services.contents_service import ContentsService
from cocoman_recommender.containers import Container

router = InferringRouter()


@cbv(router)
class ContentsController:
    @inject
    def __init__(self, contents_service: ContentsService = Depends(Provide[Container.contents_service])):
        self.contents_service = contents_service

    @router.get('/')
    async def get_all(self):
        return self.contents_service.find_all()

    @router.get('/{id}')
    async def get_by_id(self, id: int):
        return self.contents_service.find_by_id(id)

    @router.post('/')
    async def create(self, contents_dto: ContentsDto):
        return self.contents_service.create(contents_dto)

    @router.delete('/')
    async def delete(self, id: int):
        contents_dto = self.contents_service.find_by_id(id)
        if not contents_dto:
            raise HTTPException(status_code=400, detail="contents not found")
        return self.contents_service.delete(contents_dto)

    @router.put('/')
    async def update(self, contents_dto: ContentsUpdateDto):
        original_dto = self.contents_service.find_by_id(contents_dto.id)
        if not original_dto:
            raise HTTPException(status_code=400, detail="contents not found")
        return self.contents_service.update(contents_dto)
