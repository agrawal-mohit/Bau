

class MethodException(Exception):
    pass


class MissingArgs(MethodException):
    pass
    

class BaseMethod(object):
    _required = None
    _optional = None

    def __init__(self, **kwargs):
        self._verify_args(**kwargs)

    def _verify_args(self, **kwargs):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError

    @classmethod
    def params(self):
        '''
        Returns two tuples containing required and optional parameters
        '''
        if self._required is None or self._optional is None:
            raise NotImplementedError
        else:
            return self._required, self._optional

