from models.entities import Anime
from models.configs.connection import DBConnection
from interfaces import InterfaceRepository
from flask import jsonify
from flask.json import JSONEncoder


class RepositoryAnime(InterfaceRepository):
    def create(self):
        pass

    def read(self) -> dict:
        """
        This function will read all anime lines in the database, and return it.
        """

        with DBConnection() as db:
            try:
                # Get all datas into the Anime table
                data = db.session.query(Anime)

            except Exception as error:
                return error
            else:
                return list(
                    map(
                        lambda value: {
                            "id_anime": value.id_anime,
                            "name_anime": value.name_anime,
                            "description_anime": value.description_anime,
                            "criation_date_anime": value.criation_date_anime,
                            "add_date_anime": value.add_date_anime,
                            "last_modifyed_date_anime": value.last_modifyed_date_anime,
                        },
                        data,
                    )
                )

    def update(self):
        pass

    def select_one(self):
        pass

    def delete(self):
        pass
