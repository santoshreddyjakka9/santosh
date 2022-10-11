class Bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("Most of birds can fly some cannot")
class Sparrow(Bird):
    def flight(self):
        print("Sparroes can fly")

class Ostrich(Bird):
    def flight(self):
        print("ostrich cannot fly")

a=Bird()
b=Sparrow()
c=Ostrich()

a.intro()
a.flight()
b.intro()
b.flight()
c.intro()
c.flight()