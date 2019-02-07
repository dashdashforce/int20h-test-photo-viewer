from .services import service_locator
from pprint import pprint
flickr_service = service_locator.flickr_service

page = 1

response = flickr_service.fetch_sync(page)
pprint(response)
flickr_service._save_photos(response['photoset']['photo'])

for i in range((page+1), response.photoset.pages):
    flickr_service.fetch_sync(page)
