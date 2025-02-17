# Родительский класс Animal
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не может есть это.")

# Родительский класс Plant
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

# Класс-наследник Mammal
class Mammal(Animal):
    pass

# Класс-наследник Predator
class Predator(Animal):
    pass

# Класс-наследник Flower
class Flower(Plant):
    pass

# Класс-наследник Fruit
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

# Пример использования:
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

print(a1.alive)  # True
print(a2.fed)    # False
a1.eat(p1)       # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)       # Хатико съел Заводной апельсин
print(a1.alive)  # False (Волк умер, так как съел несъедобный цветок)
print(a2.fed)    # True (Хатико насытился, так как съел съедобный фрукт)