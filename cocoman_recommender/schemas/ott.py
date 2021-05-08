from sqlalchemy import (
    Column,
    Integer,
    String
)
from typing import List

from cocoman_recommender.schemas.base_repository import BaseRepository
from cocoman_recommender.schemas.conn import Base


class Ott(Base):
    __tablename__ = 'TB_OTT'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255))
    image_path = Column(String(length=255))


class OttRepository(BaseRepository):
    def __init__(self, session_factory):
        super().__init__(session_factory)

    def get_all(self) -> List[Ott]:
        with self.session_factory() as session:
            return session.query(Ott).all()

    def get_by_id(self, id: int) -> Ott:
        with self.session_factory() as session:
            return session.query(Ott).filter(Ott.id == id).one()

    def get_by_name(self, name: str):
        with self.session_factory() as session:
            return session.query(Ott).filter(Ott.name == name).one()

    def create(self, entity: Ott):
        with self.session_factory() as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity
