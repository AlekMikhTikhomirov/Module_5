class House:
    def __init__(self, name, number_of_floors):
        self.name = input("Enter the name of new house: ")
        self.number_of_floors = int(input("Enter the number of floors: "))

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Building name: {self.name}, number of floors: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors

    def go_to(self, new_floor):
        self.new_floor = int(input("Enter the floor number you want to go (or lift): "))
        if self.new_floor <= self.number_of_floors and self.new_floor >= 1:
            for i in range(self.new_floor):
                print(i+1)
        elif self.new_floor > self.number_of_floors or self.new_floor < 1:
            print("No such floor in this house")

    def __add__(self, additional_floors):
        additional_floors = int(input("Enter the number of floors you want to add: "))
        self.number_of_floors += additional_floors
        return self

    def __iadd__(self, additional_floors):
        self.__add__(0)
        return self

    def __radd__(self, additional_floors):
        self.__add__(0)
        return self

house_1 = House('', 0)
house_2 = House('', 0)

print(house_1)
print(house_2)

print(house_1 == house_2)

house_1.__add__(0)
print(house_1)
print(house_1 == house_2)

house_1.__iadd__(0)
print(house_1)

house_2.__radd__(0)
print(house_2)

print(house_1 > house_2)
print(house_1 >= house_2)
print(house_1 < house_2)
print(house_1 <= house_2)
print(house_1 != house_2)