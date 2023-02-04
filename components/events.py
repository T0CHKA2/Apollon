class Event(object):

    def __init__(self):
        self.status = False

    def set(self):
        self.status = True

    def is_set(self):
        if self.status is False or None:
            return False
        else:
            return True

    def clear(self):
        self.status = False

# Why i do this, its because i can freely modify Event settings
# Also soon there will be all Events variables