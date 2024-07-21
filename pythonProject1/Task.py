class Device:
    def __init__(self, brand):
        self.brand = brand


class CoffeMachine(Device):
    def __init__(self, brand, size, temperature):
        super().__init__(brand)
        self.size = size
        self.temperature = temperature

    def start(self):
        print(f"{self.brand} coffe machine is making {self.size} coffe with temperature {self.temperature}°C")


class Blender(Device):
    def __init__(self, brand, rpm):
        super().__init__(brand)
        self.rpm = rpm

    def start(self):
        print(f"{self.brand} blender is blending with {self.rpm} RPM")


class MeatGrinder(Device):
    def __init__(self, brand, grind_size):
        super().__init__(brand)
        self.grind_size = grind_size

    def start(self):
        print(f"{self.brand} meat grinder is grinding with {self.grind_size} grind size")


d1 = CoffeMachine("Tchibo", "large", 120)
d1.start()

d2 = Blender("Sencor", 8000)
d2.start()

d3 = MeatGrinder("Kitchen Aid", "medium")
d3.start()
