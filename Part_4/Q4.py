class Sound:
    def make_sound(self):
        print("Animal Sounds")

class Lion(Sound):
    def make_sound(self):
        print("Roaringgggggggggggg")

class Cat(Sound):
    def make_sound(self):
        print("Meowwwwwwwwwwww")

t1=Cat()
t1.make_sound()

t2 = Lion()
t2.make_sound()

t3 = Sound()
t3.make_sound()