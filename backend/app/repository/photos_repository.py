
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

    async def get_photos(self):
        return None

    """
        TODO Implement async photo caching
    """
    async def save_photos(self, photos):
        await self.collection.insert_many(photos)
