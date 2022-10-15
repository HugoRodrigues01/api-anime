from models.configs.base import Base
from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from datetime import datetime


class TypeAnime(Base):

    __tablename__: str = "tbl_type_anime"

    id_type_anime: Column = Column(
        "id_type_anime", BigInteger(), autoincrement=True, primary_key=True
    )

    type_anime: Column = Column(String(50), nullable=False, unique=True)

    add_date_type_anime: Column = Column(
        "add_date_type_anime", DateTime(timezone=True), default=datetime.utcnow
    )
    last_modifyed_date_type_anime: Column = Column(
        "last_modifyed_date_type_anime",
        DateTime(timezone=True),
        default=datetime.utcnow,
    )

    def __reper__(self) -> str:
        return f"[TypeAnime={self.type_anime}, \
                AddDateTypeAnime={self.add_date_type_anime}]"
