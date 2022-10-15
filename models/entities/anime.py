from models.configs.base import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    ForeignKey,
    TIMESTAMP,
)
from .type_anime import TypeAnime
from models.configs.connection import DBConnection
from datetime import datetime, date

# from flask.json import JSONEncoder


class Anime(Base):

    __tablename__: str = "tbl_anime"

    id_anime: Column = Column(
        "id_anime", Integer(), primary_key=True, autoincrement=True
    )
    name_anime: Column = Column("name_anime", String(50), nullable=False)
    description_anime: Column = Column("description_anime", String(200), nullable=False)
    criation_date_anime: Column = Column("criation_date_anime", Date(), nullable=False)
    add_date_anime: Column = Column(
        "add_date_anime",
        DateTime(timezone=True),
        default=datetime.utcnow,
    )
    last_modifyed_date_anime: Column = Column(
        "last_modifyed_date_anime", DateTime(), default=datetime.utcnow
    )

    def __repr__(self) -> str:

        return str(
            {
                "id_anime": self.id_anime,
                "name_anime": self.name_anime,
                "description_anime": self.description_anime,
                "criation_date_anime": self.criation_date_anime,
                "add_date_anime": self.add_date_anime,
                "last_modifyed_date_anime": self.last_modifyed_date_anime,
            }
        )
