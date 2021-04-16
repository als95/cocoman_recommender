import os.path
import shutil
from typing import List
from fastapi import UploadFile

from cocoman_recommender.config.config import BASE_DIR
from cocoman_recommender.models.contents_dto import ContentsDto, ContentsUpdateDto
from cocoman_recommender.schemas.contents import ContentsRepository, Contents
from cocoman_recommender.schemas.ott import OttRepository
from cocoman_recommender.schemas.actor import ActorRepository
from cocoman_recommender.schemas.director import DirectorRepository
from cocoman_recommender.schemas.genre import GenreRepository
from cocoman_recommender.schemas.keyword import KeywordRepository


class ContentsService:
    def __init__(self,
                 contents_repository: ContentsRepository,
                 ott_repository: OttRepository,
                 actor_repository: ActorRepository,
                 director_repository: DirectorRepository,
                 genre_repository: GenreRepository,
                 keyword_repository: KeywordRepository):
        self.contents_repository = contents_repository
        self.ott_repository = ott_repository
        self.actor_repository = actor_repository
        self.director_repository = director_repository
        self.genre_repository = genre_repository
        self.keyword_repository = keyword_repository

    def find_all(self) -> List[Contents]:
        return self.contents_repository.get_all()

    def find_by_id(self, id: int) -> Contents:
        return self.contents_repository.get_by_id(id)

    def create(self, contents_dto: ContentsDto):
        content = Contents(title=contents_dto.title,
                           year=contents_dto.year,
                           country=contents_dto.country,
                           running_time=contents_dto.running_time,
                           grade_rate=contents_dto.grade_rate,
                           broadcaster=contents_dto.broadcaster,
                           open_date=contents_dto.open_date,
                           broadcast_date=contents_dto.broadcast_date,
                           story=contents_dto.story,
                           poster_path=contents_dto.poster_path
                           )
        self.contents_repository.create(content)

    def delete(self, contents_dto: ContentsUpdateDto):
        self.contents_repository.delete(contents_dto)

    def update(self, contents_dto: ContentsUpdateDto):
        content = Contents(id=contents_dto.id,
                           title=contents_dto.title,
                           year=contents_dto.year,
                           country=contents_dto.country,
                           running_time=contents_dto.running_time,
                           grade_rate=contents_dto.grade_rate,
                           broadcaster=contents_dto.broadcaster,
                           open_date=contents_dto.open_date,
                           broadcast_date=contents_dto.broadcast_date,
                           story=contents_dto.story,
                           poster_path=contents_dto.poster_path
                           )
        self.contents_repository.update(content)
