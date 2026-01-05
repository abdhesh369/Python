class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year= year
    
    def car_info(self):
        print(f"The brand of car is {self.brand} \nModel is {self.model} \nThe year of lunch is {self.year}\n")

p1 = car("Mercedes-Benz"," 300 SL Gullwing", 1955)
p2 = car("Ford","Model A", 1903)

p1.car_info()
p2.car_info()