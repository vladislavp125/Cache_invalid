from functools import wraps
import asyncio


class Cache:
    def __init__(self):
        self.data = {}

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if args not in self.data:
                result = await func(*args, **kwargs)
                self.data[args] = result
                return result
        return wrapper

    def invalidate(self, func):
        del self.data[func]


cache = Cache()


@cache
def slow_function(arg):
    return arg


class MyClass:
    @cache
    def method(self, arg):
        return arg


@cache
async def async_func(arg):
    return arg

