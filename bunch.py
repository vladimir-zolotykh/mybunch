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
            for name in defaults:
                val = kwds.pop(name, None)
                if val is None:
                    setattr(self, name, defaults[name])
                else:
                    setattr(self, name, val)
            if kwds:
                extra = ", ".join(k for k in kwds)
                raise TypeError(f"Extra args: {extra}")

        def __repr__(self):
            args = ", ".join(
                f"{name}={val!r}"
                for name, dval in defaults.items()
                if dval != (val := getattr(self, name))
            )
            return f"{type(self).__name__}({args})"

        ns2 = {"__slots__": [], "__init__": __init__, "__repr__": __repr__}

        for name, val in ns.items():
            if name[:2] == "__" and name[-2:] == "__":
                if name in ns2:
                    raise TypeError(f"Cannot overwrite {name}")
                ns2[name] = val
            else:
                defaults[name] = val
                ns2["__slots__"].append(name)
        return super().__new__(mcls, clsname, bases, ns2)


class Bunch(metaclass=BunchMeta):
    x = 0.0
    y = 0.0
    color = "gray"


if __name__ == "__main__":
    # b1 = Bunch(x=1, y=2, z=3, color="gray")
    b1 = Bunch(x=1.0)
    print(b1)
