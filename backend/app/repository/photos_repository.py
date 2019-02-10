
import os

from dotenv import find_dotenv, load_dotenv
from motor.motor_tornado import MotorClient

load_dotenv(find_dotenv())


class PhotosRepository():
    def __init__(self):
        db_url = os.getenv("MONGODB_URL")
        db_name = os.getenv("MONGODB_DB")
        self.db_client = MotorClient(db_url)[db_name]
        self.collection = self.db_client.photos

    """
        TODO Implement cached photo async retrieving. Maybe add some page arguments
    """

    async def get_photos(self, first, after):
        if after:
            after_photo = await self.collection.find_one({'id': after})
            return await self.collection.find(
                {
                    'dateupload': {'$lt': after_photo['dateupload']}
                }

            ).sort('dateupload').to_list(length=first)
        else:
            return await self.collection.find().sort('dateupload').to_list(length=first)

    """
        TODO Implement optimize update or insert operation
    """

    async def save_photos(self, photos):

        await self.collection.insert_many(
            map(self._normalize_photo, photos),
            bypass_document_validation=True
        )

    def _normalize_photo(self, photo):
        photo['_id'] = photo['id']
        return photo
