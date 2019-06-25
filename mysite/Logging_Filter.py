import logging
from django.conf import settings

# creates a filter class so that the logger is able to recognise certain errors.
class ErrorFilter(logging.Filter):

    #filters out the 404 errrors and 500 errors so that they can be succesffuly logged
    def filter(self, record):
        if record.args[1].startswith('404'):
            return True
        if record.args[1].startswith('/errors/404'):
            return True
        if record.args[1].startswith('500'):
            return True
        if record.args[1].startswith('/errors/500'):
            return True
        return False