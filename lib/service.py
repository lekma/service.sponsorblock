# -*- coding: utf-8 -*-


from iapc import public, Service


# ------------------------------------------------------------------------------
# SponsorBlockService

class SponsorBlockService(Service):

    def __init__(self, *args, **kwargs):
        super(SponsorBlockService, self).__init__(*args, **kwargs)

    def __setup__(self):
        pass

    def __stop__(self):
        self.logger.info("stopped")

    def start(self, **kwargs):
        self.logger.info("starting...")
        self.__setup__()
        self.serve(**kwargs)
        self.__stop__()

    def onSettingsChanged(self):
        self.__setup__()


# __main__ ---------------------------------------------------------------------

if __name__ == "__main__":
    SponsorBlockService().start()
