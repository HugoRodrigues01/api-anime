from abc import ABC, abstractmethod
from typing import Union
from sqlalchemy.orm.exc import NoResultFound


class InterfaceRepository(ABC):
    @abstractmethod
    def create(self) -> dict:
        pass

    @abstractmethod
    def read(self) -> dict:
        pass

    @abstractmethod
    def update(self) -> dict:
        pass

    @abstractmethod
    def delete(self) -> dict:
        pass
