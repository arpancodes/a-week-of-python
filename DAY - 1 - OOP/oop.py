# class is blueprint of objects

# we can instantiate multiple "unique" object from a single class

# class contains properties and methods

# constructor or "__init__"

# 4 pillars of OOP:

# 1. Encapsulation

# 2. Abstraction

# 3. Inheritance

# 4. Polymorphism

# BONUS: dunder methods and multiple inheritance, mro


# |^^^^^^^^^^^^^^^^^|  instantiate
# |                 |  -----------> Object1 - properties, methods
# |      CLASS      |
# |    properties   |  -----------> Object2 - properties, methods
# |     methods     |
# |                 |  -----------> Object3 - properties, methods
# |_________________|

class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f'[FROM FATHER] {self.name} Walking...')


class Mother:
    def __init__(self, hair_color):
        self.hair_color = hair_color

    def sprint(self):
        print(f'[FROM MOTHER] Sprinting...')


class Son(Father, Mother):
    def __init__(self, name, age, hair_color):
        Mother.__init__(self, hair_color)
        Father.__init__(self, name, age)

    def fight(self):
        print(f'{self.name} is using - Nutcracker choke')


class Daugter(Father):
    def __init__(self, name, age):
        super().__init__(name, age)

    def fight(self):
        print(f'{self.name} is using - Ax stomp to the wherever')


jarrard = Son('Jarrard', 10, 'blak')
daisy = Daugter('Daisy', 12)

jarrard.sprint()
jarrard.walk()


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.__mro__)
