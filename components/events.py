class Event(object):

    def __init__(self):
        self.status = False

    def set(self):
        """
        Setting event to True status.
        """
        self.status = True

    def is_set(self):
        """
        Check event status. Return True if set.
        """
        if self.status is False or None:
            return False
        else:
            return True

    def clear(self):
        """
        Setting event to False
        """
        self.status = False

# Why i do this, its because i can freely modify Event settings
# Also soon there will be all Events variables