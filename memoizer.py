import LRUCache

__methods__ = {'LRU': LRUCache.LRUCache}


class MemoizerException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Memoizer:
    def __init__(self, *parms):
        if len(parms) != 2:
            raise MemoizerException("You have to specify method and size. Eg LRU,3")
        self._cache = __methods__[parms[0]](parms[1])

    def __call__(self, function):
        def memoizer(*args):
            if not self._cache.get(args):
                self._cache.put(args, function(*args))
            return self._cache.get(args)

        return memoizer
