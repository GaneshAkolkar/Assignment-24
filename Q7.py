class Laptop:
    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def showConfig(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}GB, CPU: {self.cpu}, HDD: {self.hdd}GB")
