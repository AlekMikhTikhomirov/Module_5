class House:
    def __init__(self, name, number_of_floors):
        self.name = input("Enter the name of new house: ")
        self.number_of_floors = int(input("Enter the number of floors: "))

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Building name: {self.name}, number of floors: {self.number_of_floors}"

    def go_to(self, new_floor):
        self.new_floor = int(input("Enter the floor number you want to go (or lift): "))
        if self.new_floor <= self.number_of_floors and self.new_floor >= 1:
            for i in range(self.new_floor):
                print(i+1)
        elif self.new_floor > self.number_of_floors or self.new_floor < 1:
            print("No such floor in this house")

house_1 = House('', 0)
house_1.go_to(0)
print(house_1)
print(len(house_1))