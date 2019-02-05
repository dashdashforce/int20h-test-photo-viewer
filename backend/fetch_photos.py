from src.services import FlickApiService
from pprint import pprint
flickr_service = FlickApiService()    

page = 1

response = flickr_service.fetch_sync(page)
pprint(response)
flickr_service.save_photos(response['photoset']['photo'])

for i in range((page+1), response.photoset.pages):
    flickr_service.fetch_sync(page)