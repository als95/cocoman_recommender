from typing import List

from cocoman_recommender.models.contents_dto import ContentsDto
from cocoman_recommender.schemas.contents import ContentsRepository, Contents
from cocoman_recommender.schemas.ott import Ott
from cocoman_recommender.schemas.actor import Actor
from cocoman_recommender.schemas.director import Director
from cocoman_recommender.schemas.genre import Genre
from cocoman_recommender.schemas.keyword import Keyword

from cocoman_recommender.models.update_contents_title_dto import UpdateContentsTitleDto


class ContentService:
    def __init__(self, contents_repository: ContentsRepository):
        self.contents_repository = contents_repository

    # def find_all(self) -> List[ContentsDto]:
    #     return self.contents_repository.get_all()

    def create(self, contents_dto: ContentsDto):
        contents = Contents(title=contents_dto.title, year=contents_dto.year, country=contents_dto.country,
                            running_time=contents_dto.running_time, grade_rate=contents_dto.grade_rate,
                            broadcaster=contents_dto.broadcaster, open_date=contents_dto.open_date,
                            broadcast_date=contents_dto.broadcast_date, story=contents_dto.story,
                            poster_path=contents_dto.poster_path)

        return self.contents_repository.create(contents)


    def update_title(self,update_contents_dto: UpdateContentsTitleDto):
        id = update_contents_dto.id
        title = update_contents_dto.title

        self.contents_repository.update_title(id, title)
