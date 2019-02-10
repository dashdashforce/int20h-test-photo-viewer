from collections import defaultdict

from app.clients import FlickrApiClient
from app.repository import PhotosRepository

from app.utils import merge_list_of_records_by


def merge_photos_by_id(first, second):
    merger = merge_list_of_records_by('id', lambda first, second: first)
    return merger(first + second)


class PhotoFetchingJob:
    def __init__(self):
        self.flickr_client = FlickrApiClient()
        self.photos_repository = PhotosRepository()

    async def start(self):
        photos = []
        print('fetching first album page')
        first_album_page = await self.flickr_client.fetch_album_photos(1, 500)
        pages = first_album_page['pages']
        print('fetched {} photos, total pages: {}, total photos: {}'.format(
            len(first_album_page['photo']),
            pages,
            first_album_page['total']
        ))
        photos = merge_photos_by_id(photos, first_album_page['photo'])

        for page in range(1, pages):
            print('fetching {} page'.format(page))
            album_page = await self.flickr_client.fetch_album_photos(page, 500)
            photos = merge_photos_by_id(photos, album_page['photo'])
            print('fetched {} photos'.format(
                len(album_page['photo'])
            ))
        print('Photos count: {}'.format(len(photos)))

        print('fetching first search page')
        first_tag_page = await self.flickr_client.fetch_photos_by_tag(1, 500)
        pages = first_tag_page['pages']
        print('fetched {} photos, total pages: {}, total photos: {}'.format(
            len(first_tag_page['photo']),
            pages,
            first_tag_page['total']
        ))
        photos = merge_photos_by_id(photos, first_tag_page['photo'])
        for page in range(1, pages):
            print('fetching {} page'.format(page))
            search_page = await self.flickr_client.fetch_photos_by_tag(page, 500)
            photos = merge_photos_by_id(photos, search_page)
            print('fetched {} photos'.format(
                len(search_page['photo'])
            ))

        print('Photos count: {}'.format(len(photos)))
        await self.photos_repository.save_photos(photos)
