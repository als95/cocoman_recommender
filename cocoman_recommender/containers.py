from dependency_injector import containers, providers

from dataclasses import asdict
from cocoman_recommender.config.config import conf
from cocoman_recommender.schemas.conn import SQLAlchemy
from cocoman_recommender.schemas.ott import OttRepository
from cocoman_recommender.schemas.actor import ActorRepository
from cocoman_recommender.services.ott_service import OttService
from cocoman_recommender.services.acter_service import ActorService


class Container(containers.DeclarativeContainer):
    c = conf()
    conf_dict = asdict(c)

    """ Database """
    db = providers.Singleton(SQLAlchemy, conf_dict['DB_URL'])

    """ Repository """
    ott_repository = providers.Factory(OttRepository, session=db.provided.session)
    actor_repository = providers.Factory(ActorRepository, session_factory=db.provided.session)

    """ Service """
    ott_service = providers.Factory(OttService, ott_repository=ott_repository)
    actor_service = providers.Factory(ActorService, actor_repository=actor_repository)
