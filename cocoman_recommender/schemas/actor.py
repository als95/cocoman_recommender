from sqlalchemy import (
    Column,
    Integer,
    String
)
from typing import List
from sqlalchemy.orm import relationship

from cocoman_recommender.schemas.base_repository import BaseRepository
from cocoman_recommender.schemas.contents import contents_actor
from cocoman_recommender.schemas.conn import Base


class Actor(Base):
    __tablename__ = 'TB_ACTOR'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), nullable=False)
    image_path = Column(String(length=255))
    contents_set = relationship('Contents', secondary=contents_actor, back_populates='actors_id')


class ActorRepository(BaseRepository):
    def __init__(self, session_factory):
        super().__init__(session_factory)


    def get_all(self) -> List[Actor]:
        return self.session.query(Actor).all()

    def get_by_id(self, id: int):
        with self.session_factory() as session:
            return session.query(Actor).get(id=id)

    def create(self, entity: Actor):
        with self.session_factory() as session:
            session.add(entity)
            session.commit()

    def delete_by_id(self, id: int):
        with self.session_factory() as session:
            session.query(Actor).filter(Actor.id == id).delete(synchronize_session='fetch')   # 왜 편집기에 자동완성 안되냐..
            session.commit()

    def update(self, id: int, entity: Actor):
        with self.session_factory() as session:
            actor_query = session.query(Actor).filter(Actor.id == id)
            actor_query.update({'name': entity.name,
                                'image_path': entity.image_path,
                                #'contents_set': entity.contents_set,
            }, synchronize_session='fetch')

