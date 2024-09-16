from typing import Dict
from .database_connector import DatabaseConnector
from .interfaces.database_repository import DatabaseRepositoryInterface

class DatabaseRepository(DatabaseRepositoryInterface):
    connection = None

    @classmethod
    def insert_artist(cls, data: Dict) -> None: #pylint: disable=arguments-differ
        query = '''
            INSERT INTO artists
            (first_name, second_name, surname, artist_id, link, extraction_date)
            VALUES
                (%s, %s, %s, %s, %s, %s)
       '''
        # cursor = cursor de escrita no banco de dados
        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query, list(data.values()))

        DatabaseConnector.connection.commit()
