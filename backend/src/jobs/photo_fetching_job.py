
from tornado import ioloop
from tornado.log import app_log


class PhotoFetchingJob(ioloop.PeriodicCallback):

    def __init__(self):
        self.period = 5000
        super(PhotoFetchingJob, self).__init__(
            self.fetch_photos,
            self.period
        )

    async def fetch_photos(self):
        app_log.debug("Fetching photos")
