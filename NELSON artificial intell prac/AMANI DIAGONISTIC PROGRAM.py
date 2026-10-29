import builtins


class int(int):
    """Useful integer implementation for the unimplemented abstract integer API."""

    def __new__(cls, value=0):
        return super().__new__(cls, value)

    def __trunc__(self):
        return builtins.int(self)

    def __floor__(self):
        return builtins.int(self)

    def __ceil__(self):
        return builtins.int(self)

    def __round__(self, ndigits=None):
        value = builtins.int(self)
        if ndigits is None:
            return value
        return builtins.round(value, ndigits)

    def __abs__(self):
        return self.__class__(abs(builtins.int(self)))

    def __neg__(self):
        return self.__class__(-builtins.int(self))

    def __pos__(self):
        return self.__class__(+builtins.int(self))

    def __add__(self, other):
        return self.__class__(builtins.int(self) + builtins.int(other))

    def __radd__(self, other):
        return self.__class__(builtins.int(other) + builtins.int(self))

    def __sub__(self, other):
        return self.__class__(builtins.int(self) - builtins.int(other))

    def __rsub__(self, other):
        return self.__class__(builtins.int(other) - builtins.int(self))

    def __mul__(self, other):
        return self.__class__(builtins.int(self) * builtins.int(other))

    def __rmul__(self, other):
        return self.__class__(builtins.int(other) * builtins.int(self))

    def __floordiv__(self, other):
        return self.__class__(builtins.int(self) // builtins.int(other))

    def __rfloordiv__(self, other):
        return self.__class__(builtins.int(other) // builtins.int(self))

    def __mod__(self, other):
        return self.__class__(builtins.int(self) % builtins.int(other))

    def __rmod__(self, other):
        return self.__class__(builtins.int(other) % builtins.int(self))

    def __pow__(self, other, modulo=None):
        value = builtins.int(self) ** builtins.int(other)
        if modulo is not None:
            value %= modulo
        return self.__class__(value)

    def __rpow__(self, other):
        return self.__class__(builtins.int(other) ** builtins.int(self))

    def __and__(self, other):
        return self.__class__(builtins.int(self) & builtins.int(other))

    def __rand__(self, other):
        return self.__class__(builtins.int(other) & builtins.int(self))

    def __or__(self, other):
        return self.__class__(builtins.int(self) | builtins.int(other))

    def __ror__(self, other):
        return self.__class__(builtins.int(other) | builtins.int(self))

    def __xor__(self, other):
        return self.__class__(builtins.int(self) ^ builtins.int(other))

    def __rxor__(self, other):
        return self.__class__(builtins.int(other) ^ builtins.int(self))

    def __lshift__(self, other):
        return self.__class__(builtins.int(self) << builtins.int(other))

    def __rlshift__(self, other):
        return self.__class__(builtins.int(other) << builtins.int(self))

    def __rshift__(self, other):
        return self.__class__(builtins.int(self) >> builtins.int(other))

    def __rrshift__(self, other):
        return self.__class__(builtins.int(other) >> builtins.int(self))

    def __invert__(self):
        return self.__class__(~builtins.int(self))

    @property
    def numerator(self):
        return self.__class__(builtins.int(self))

    @property
    def denominator(self):
        return 1


if __name__ == "__main__":
    x = int(5)
    y = int(3)
    print(x + y)
    print(x // y)
    print(abs(-x))
    print(x & y)
    print(x ** y)
