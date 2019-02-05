
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

class PhotosRepository():
    def __init__(self):

        self.collection = ((MongoClient(os.getenv("MONGODB_URL")))[os.getenv("MONGODB_DB")]).photos


    def batch_insert(self, photos):
        
        self.collection.insert_many(photos)

