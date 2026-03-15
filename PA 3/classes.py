class Flower():
    def __init__(self,
                 name:str,
                 petals:int,
                 color:str,
                 height:int
                 ):
        self.name = name
        self.petals = petals
        self.color = color
        self.height = height

    def describe(self):
        print(f'{self.name} is {self.color}, has {self.petals} petals, and is {self.height} cm tall.')

    def grow(self):
        self.height += 2

flower_one = Flower("rose", 5, "red", 10 )
flower_two = Flower("tulip", 7, "blue", 15 )
flower_three = Flower("daizy", 3, "yellow", 7 )
flower_four = Flower("lily", 8, "orange", 17 )
garden = [flower_one, flower_two, flower_three, flower_four]

for flower in garden:
    flower.describe()
    flower.grow()
    print("growing...")
    flower.describe()

