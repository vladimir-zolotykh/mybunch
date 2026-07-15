#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> class Point(Bunch):
...     x = 0.0
...     y = 0.0
...     color = 'gray'
...
>>> Point(x=1.2, y=3, color='green')
Point(x=1.2, y=3, color='green')
>>> p = Point()
>>> p.x, p.y, p.color
(0.0, 0.0, 'gray')
>>> p
Point()
>>> Point(x=1, y=2, z=3)
Traceback (most recent call last):
  ...
AttributeError: No slots left for: 'z'
>>> p = Point(x=21)
>>> p.y = 42
>>> p
Point(x=21, y=42)
>>> p.flavor = 'banana'
Traceback (most recent call last):
  ...
AttributeError: 'Point' object has no attribute 'flavor'

"""


class BunchMeta(type):
    def __new__(mcls, clsname, bases, ns):
        defaults = {}

        def __init__(self, *args, **kwds):
            """Initialize only attributes in defaults"""
            pass

        def __repr__(self):
            """Print attributes only if they differ from defaults"""
            pass

        ns2 = {"__slots__": [], "__init__": __init__, "__repr__": __repr__}

        for key, val in ns.items():
            pass
        return super().__new__(mcls, clsname, bases, ns2)


if __name__ == "__main__":
    pass
