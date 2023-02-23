class Display:
    def __init__(self):
        self._msg = ''

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def reset(self):
        self.msg = ''

    def __str__(self):
        return str(self.msg)

    __repr__ = __str__
