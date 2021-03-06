from ..core.flow import *
from ..core.utils import *
from sys import version_info
from functools import reduce

try:
    from cytoolz import compose
except (ModuleNotFoundError if version_info.minor >= 6 else ImportError):
    def compose(*fns):
        def call(e):
            return reduce(lambda x, y: y(x), fns[::-1], e)

        return call
_ext_list = extension_class(list)

src = ''


@_ext_list
def Extended(self: list, *others):
    stream = self.copy()
    for other in map(unbox_if_flow, others):
        stream.extend(other)
    return stream


@_ext_list
def Extend(self: list, *others):
    for other in map(unbox_if_flow, others):
        self.extend(other)
    return self


@_ext_list
def Sort(self: list, by=None):
    if by and is_to_destruct(by):
        by = destruct_func(by)
    self.sort(key=by)
    return self


@_ext_list
def Reverse(self: list):
    self.reverse()
    return self


@_ext_list
def Reversed(self: list):
    return self[::-1]


@_ext_list
def ArgSorted(self: list, by=None):
    if by is None:
        return sorted(range(len(self)), key=self.__getitem__)
    if is_to_destruct(by):
        by = destruct_func(by)
    return sorted(range(len(self)), key=compose(by, self.__getitem__))


@_ext_list
def First(self: list):
    try:
        return self[0]
    except IndexError:
        return None


@_ext_list
def Skip(self: list, n: int):
    return self[n:]


@_ext_list
def Drop(self: list, n: int):
    return self[:-n]


@_ext_list
def Shift(self: list, n: int):
    return [*self[n:], *self[:n]]


@_ext_list
def Concat(self: list, *others: list):
    self = self.copy()
    for other in others:
        self.extend(other)
    return self


@_ext_list
def ToList(self: dict):
    return self.copy()
