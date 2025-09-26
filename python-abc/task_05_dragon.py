# Mixins class
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Flymixin class


class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Dragon class


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
