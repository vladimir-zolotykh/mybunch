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

        def __init__(self, **kwds):
            if set(defaults) == set(kwds):
                self.__dict__.update(kwds)
            else:
                raise TypeError(f"Can init only {defaults}")

        def __repr__(self):
            changed = []
            for name, dval in defaults.items():
                val = getattr(self, name)
                if val == dval:
                    continue
                else:
                    changed.append(val)
            args = ", ".join(f"{x}" for x in changed)
            return f"type(self).__name__({args})"

        ns2 = {"__slots__": [], "__init__": __init__, "__repr__": __repr__}

        for name, val in ns.items():
            if name[:2] == "__" and name[-2:] == "__":
                if name in ns2:
                    raise TypeError(f"Cannot overwrite {name}")
                ns2[name] = val
            defaults[name] = val
            ns2["__slots__"].append(name)
        return super().__new__(mcls, clsname, bases, ns2)


class Bunch(metaclass=BunchMeta):
    x = 0.0
    y = 0.0
    color = "gray"


if __name__ == "__main__":
    b1 = Bunch()
    print(b1)
