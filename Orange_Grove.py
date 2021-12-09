import random

class Order:
    
    def __init__(self, orange_wanted):
        self.orange_wanted = orange_wanted
        self.num_oranges = 0
        self.total_weight = 0

    def oranges(self):
        for i in range(self.orange_wanted):
            weight = random.uniform(96, 184)
            if self.total_weight + weight > 140000:
                break
            else:
                self.num_oranges += 1
                self.total_weight += weight
    
    def __repr__(self):
        return("There are " + str(self.num_oranges) + " oranges, and the total weight is " + str(round(self.total_weight/1000, 3)) + " kilograms.")

order1 = Order(1000)
order1.oranges()
print(order1)

order1.oranges()
print(order1)

order1.oranges()
print(order1)
