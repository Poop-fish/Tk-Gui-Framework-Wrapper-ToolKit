from GTG_imports import *
import time
class TimeMod:
    def __init__(self):
        """Custom time class to get current time in milliseconds."""
        self.value = time.time() * 1000  # Store time in milliseconds

    def __float__(self):
        """Allows conversion using float()."""
        return self.value

    def __int__(self):
        """Allows conversion using int()."""
        return int(self.value)

    def __repr__(self):
        return f"TimeMod({self.value})"

    def now(self):
        """Returns the current time in milliseconds."""
        self.value = time.time() * 1000
        return self

class IntMod:
    def __init__(self, value):
        """Custom integer-like class that mimics int behavior."""
        self.value = int(value)

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"IntMod({self.value})"

    def __add__(self, other):
        return IntMod(self.value + int(other))

    def __sub__(self, other):
        return IntMod(self.value - int(other))

    def __mul__(self, other):
        return IntMod(self.value * int(other))

    def __mod__(self, other):
        return IntMod(self.value % int(other))

    def __eq__(self, other):
        return self.value == int(other)

    def __lt__(self, other):
        return self.value < int(other)

    def __le__(self, other):
        return self.value <= int(other)

    def __gt__(self, other):
        return self.value > int(other)

    def __ge__(self, other):
        return self.value >= int(other)

class Random_Mod:
    def __init__(self, seed=None):
        if seed is None:
            seed = IntMod(TimeMod().now())  
        self.seed = seed

    def _next(self):
        self.seed = (1664525 * int(self.seed) + 1013904223) % (2**32)
        return self.seed

    def uniform(self, a, b):
        """Returns a random float in range [a, b]."""
        return a + (self._next() / (2**32)) * (b - a)

#* \\ global instance 
GTG_Random = Random_Mod()

