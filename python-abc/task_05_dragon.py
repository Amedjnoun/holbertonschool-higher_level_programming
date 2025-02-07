#!/usr/bin/python3

class SwimMixin:
    """
    Mixin class with swim method.
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class with fly method.
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class inheriting from both SwimMixin and FlyMixin.
    """
    def roar(self):
        print("The dragon roars!")
