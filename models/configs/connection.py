from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Engine
from typing import Type

CONNECTION_STRING: str = "mysql+pymysql://root:root123@localhost/db_teste"
DEBUG: bool = False


class DBConnection:
    def __init__(self) -> None:

        self.__connection_string: str = CONNECTION_STRING
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string, echo=DEBUG)

        return engine

    def get_engine(self):
        print(type(self.__engine))
        return self.__engine

    def __enter__(self):

        session_maker: sessionmaker = sessionmaker(bind=self.__engine)
        self.session = session_maker()

        return self

    def __exit__(self, exc_type, exc_value, exc_tb):

        self.session.close()


if __name__ == "__main__":
    db = DBConnection()
    print(db.get_engine())
