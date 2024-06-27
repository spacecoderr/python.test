class Animal:
    def __init__(self):
        self.num_eyes=2
    def breathe(self):
        print("INHALE,EXHALE")
class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
         print("moving in water")
creature=Fish()
creature.swim()
creature.breathe()
print(creature.num_eyes)            
