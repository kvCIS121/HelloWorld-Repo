class Duck:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, new_color):
        self.color = new_color
    
    def speak(self):
        print("quack")
    
    def __str__(self):
        return f'Duck(name={self.name}, color={self.color})'


class Pond:
    def __init__(self, name):
        self.name = name
        self.ducks = []

    def add_duck(self, duck):
        self.ducks.append(duck)

    def ducks_quack(self):
        for duck in self.ducks:
            duck.speak()
    
    def __str__(self):
        return f'Pond(name={self.name}, ducks={len(self.ducks)})'


duck1 = Duck('Donald', 'Blue')
duck2 = Duck('Scrooge', 'Black')

pond1 = Pond('Whispering Waters')

pond1.add_duck(duck1)
pond1.add_duck(duck2)

pond1.ducks_quack()
print(pond1)
