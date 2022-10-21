class car():
    def __init__(self, brand, color, mileage):
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):

        print(self.brand)

    def set_brand(self, new_brand):

        self.brand = new_brand    

a_car = car("volvo", "blå", 12000)
a_car.get_brand()
a_car.set_brand("Volvo")
a_car.get_brand()
b_car = car("Mazda", "röd", 17000)
b_car.get_brand()
b_car.set_brand("Mazda")
b_car.get_brand()
