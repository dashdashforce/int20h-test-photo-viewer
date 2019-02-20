
import logging
from traitlets.config.application import Application, catch_config_error

from .settings import LOG_NAME, DEBUG, PORT, app_log


class PhotoViewerApplication(Application):

    debug = DEBUG

    def _log_level_default(self):
        if self.debug:
            return logging.DEBUG
        else:
            return logging.INFO

    def _log_datefmt_default(self):
        return "%H:%M:%S"

    def _log_format_default(self):
        return (u'%(color)s[%(levelname)1.1s %(asctime)s.%(msecs).03d '
                u'%(name)s]%(end_color)s %(message)s')

    def init_logging(self):
        self.log.propagate = False

        logger = logging.getLogger(LOG_NAME)
        logger.propagate = True
        logger.parent = self.log
        logger.setLevel(self.log.level)

    def start(self):
        super(PhotoViewerApplication, self).start()

        self.log.info('Server started on port: {}'.format(PORT))
        self.log.debug('Debug mode: {}'.format(self.debug))

        try:
            pass
        except KeyboardInterrupt:
            self.log.info('PhotoViewerApplication interrupted...')

    def stop(self):
        pass


main = launch_new_instance = PhotoViewerApplication.launch_instance
