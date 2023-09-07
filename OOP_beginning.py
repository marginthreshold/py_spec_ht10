class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.__class__.__name__} {self.name} {self.age}'


class Dog(Animal):
    def __init__(self, name, age, color, sound="Wuf"):
        super().__init__(name, age)
        self.sound = sound
        self.color = color

    def __str__(self):
        return f'{self.__class__.__name__} {self.name} {self.age} {self.color} {self.sound}'


class Cat(Animal):
    def __init__(self, name, age, color, sound="Meo"):
        super().__init__(name, age)
        self.sound = sound
        self.color = color

    def __str__(self):
        return f'{self.__class__.__name__} {self.name} {self.age} {self.color} {self.sound}'


class Fish(Animal):
    def __init__(self, name, age, color, sound=None):
        super().__init__(name, age)
        self.sound = sound
        self.color = color

    def __str__(self):
        return f'{self.__class__.__name__} {self.name} {self.age} {self.color} {self.sound}'


def create_animal(animal_type_name, *args):
    created_class = globals()[animal_type_name]
    return created_class(*args)


if __name__ == '__main__':
    print(create_animal("Dog", "Pups", 2, "red"))
    print(create_animal("Cat", "Marusia", 4, "dark"))
    print(create_animal("Fish", "Bob", 3, "white"))
