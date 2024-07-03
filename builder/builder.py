class House:
    def __init__(self, doors: int, windows: int, garage: bool, garden: bool):
        self.doors = doors
        self.windows = windows
        self.garage = garage
        self.garden = garden

class HouseBuilder:
    def __init__(self):
        self.doors = 0
        self.windows = 0
        self.garage = False
        self.garden = False

    def set_doors(self, doors: int):
        self.doors = doors
        return self

    def set_windows(self, windows: int):
        self.windows = windows
        return self

    def set_garage(self, garage: bool):
        self.garage = garage
        return self

    def set_garden(self, garden: bool):
        self.garden = garden
        return self

    def build(self) -> House:
        return House(self.doors, self.windows, self.garage, self.garden)

# Uso
builder = HouseBuilder()
house = (builder
         .set_doors(4)
         .set_windows(10)
         .set_garage(True)
         .set_garden(True)
         .build())

print(f'House: doors={house.doors}, windows={house.windows}, garage={house.garage}, garden={house.garden}')
# Salida: House: doors=4, windows=10, garage=True, garden=True
