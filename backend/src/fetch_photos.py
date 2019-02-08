from .services import service_locator
from pprint import pprint
photo_service = service_locator.photo_service

page = 1

response = photo_service.fetch_sync(page)
pprint(response)
photo_service._save_photos(response['photoset']['photo'])

for i in range((page+1), response.photoset.pages):
    photo_service.fetch_sync(page)
