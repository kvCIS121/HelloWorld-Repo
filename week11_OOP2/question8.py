class Lion:
    def __init__(self, name, gender):
        self.name = name 
        self.gender = gender
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
    
    def roar(self):
        print(f'A lion says "Roar!" ')
    
    #summary of this object
    def __str__(self):
        return f'Lion(name = {self.name}, gender = {self.gender})'

class Zoo:
    def __init__(self, location):
        self.location = location
        self.lions = []

    def add_lion(self, lion):
        self.lions.append(lion)
    
    def lions_roar(self):
        for lion in self.lions:
            lion.roar()
        
    def count_lions(self):
        males = 0
        females = 0
        for lion in self.lions:
            if lion.gender == 'male':
                males += 1
            else:
                females += 1

        print(f'{males} male lion and {females} female lions')
            
    def __str__(self):
        return f'Zoo(location = {self.location})'

#objects for lions
lion_1 = Lion('leo', 'male')
lion_2 = Lion('lily', 'female')
lion_3 = Lion('lisa', 'female')
lion_4 = Lion('lola', 'female')
lion_5 = Lion('laury', 'female')

#objects for zoo
zoo_1 = Zoo('Minnesota Zoo')

#adding lions to the zoo
zoo_1.add_lion(lion_1)
zoo_1.add_lion(lion_2)
zoo_1.add_lion(lion_3)
zoo_1.add_lion(lion_4)
zoo_1.add_lion(lion_5)

#execute program
zoo_1.count_lions()
print(zoo_1)


