from typing import List
from fastapi import Depends, APIRouter
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from dependency_injector.wiring import inject, Provide

from cocoman_recommender.models.contents_dto import ContentsDto
from cocoman_recommender.models.update_contents_title_dto import UpdateContentsTitleDto
from cocoman_recommender.services.contents_service import ContentService
from cocoman_recommender.containers import Container

router = APIRouter()


@cbv(router)
@inject
class ContentsController:
    def __init__(self, contents_service: ContentService = Depends(Provide[Container.contents_service])):
        self.contents_service = contents_service

    @router.post('/contents/test')
    async def test(self):
        return {"message": "Content Test"}

    # @router.post('/contents/all', response_model=List[ContentsDto])
    # async def get_all(self):
    #     return self.contents_service.find_all()

    @router.post('/contents/create')
    async def create_content(self, contents_dto: ContentsDto):
        return self.contents_service.create(contents_dto)


    @router.post('/contents/updateTitle')
    async def create_content(self, update_contents_dto: UpdateContentsTitleDto):
        return self.contents_service.update_title(update_contents_dto)


