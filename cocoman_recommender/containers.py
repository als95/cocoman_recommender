from dependency_injector import containers, providers

from dataclasses import asdict
from cocoman_recommender.config.config import conf

from cocoman_recommender.schemas.ott import OttRepository
from cocoman_recommender.services.ott_service import OttService

from cocoman_recommender.schemas.contents import ContentsRepository
from cocoman_recommender.services.contents_service import ContentService

from cocoman_recommender.schemas.conn import Database

class Container(containers.DeclarativeContainer):
    c = conf()
    conf_dict = asdict(c)

    """ Database """
    db = providers.Singleton(Database, conf_dict['DB_URL'])

    """ Repository """
    ott_repository = providers.Factory(OttRepository, session_factory=db.provided.session)
    contents_repository = providers.Factory(ContentsRepository, session_factory=db.provided.session)

    """ Service """
    ott_service = providers.Factory(OttService, ott_repository=ott_repository)
    contents_service = providers.Factory(ContentService, contents_repository=contents_repository)
