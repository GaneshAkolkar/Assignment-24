laptop1 = Laptop("Dell", 8, "i5", 256)
laptop2 = Laptop("HP", 16, "i7", 512)
laptop3 = Laptop("Lenovo", 4, "i3", 128)

laptops = [laptop1, laptop2, laptop3]
sorted_laptops = sorted(laptops, key=lambda laptop: laptop.ram)
for laptop in sorted_laptops:
    laptop.showConfig()
