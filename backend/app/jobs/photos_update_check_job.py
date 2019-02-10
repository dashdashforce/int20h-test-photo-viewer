
from tornado import ioloop
from tornado.log import app_log

from app.clients import FlickrApiClient
from app.repository import PhotosRepository


class PhotosUpdateCheckJob(ioloop.PeriodicCallback):

    def __init__(self):
        self.period = 30000
        self.repository = PhotosRepository()
        self.client = FlickrApiClient()
        super(PhotosUpdateCheckJob, self).__init__(
            self.fetch_photos,
            self.period
        )

    """
        TODO implement flickr api the most recent photo fetching
    """
    async def fetch_photos(self):
        latest_photo = await self.repository.get_photos(1, None)
        page = 1
        search_page = (await self.client.fetch_photos_by_tag(page, 20))['photo']
        if search_page and latest_photo:
            while search_page[0]['dateupload'] > latest_photo[0]['dateupload']:
                app_log.info('New photo detected')
                page += 1
                await self.repository.save_photos(search_page)
                search_page = (await self.client.fetch_photos_by_tag(
                    page, 20))['photo']
