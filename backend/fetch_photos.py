
import tornado.ioloop
from app.jobs import PhotoFetchingJob

job = PhotoFetchingJob()

loop = tornado.ioloop.IOLoop.current()
loop.run_sync(job.start)
