class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        dom = super().__new__(cls)
        cls.houses_history.append(args[0])
        return dom

    def __init__(self, name, year_built):
        self.name = name
        self.year_built = year_built

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)

del h2
del h3

print(House.houses_history)
