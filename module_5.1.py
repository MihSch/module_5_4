class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __eq__(self, other):
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return isinstance(other, House) and self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return isinstance(other, House) and self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return isinstance(other, House) and self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return isinstance(other, House) and self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return isinstance(other, House) and self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += int(value)
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __len__(self):
        return int(self.number_of_floors)

    def __str__(self):
        return str(f'Название: {self.name}, кличество этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        for i in range(1, int(new_floor + 1)):
            if new_floor > self.number_of_floors or new_floor == 0:
                print('Такого этажа не существует')
                break
            else:
                print(i)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h1
del h2

print(House.houses_history)