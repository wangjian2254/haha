
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

class WeibopError(Exception):
    """Weibopy exception"""

    def __init__(self, reason):
        self.reason = reason.encode('utf-8')
#        self.reason = reason

    def __str__(self):
#        if self.reason.code:
#            return self.reason.code
        return self.reason

