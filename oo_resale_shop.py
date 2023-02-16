class ResaleShop:
    # What attributes will it need?
    inventory: list
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list):
        self.inventory = []

    def addInventory(self, computer):
        self.inventory.append(computer)

    def removeInventory(self, computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Computer not found.")
        
    def priceUpdate(self, computer, new_price):
        if computer in self.inventory:
            computer.price = new_price
        else:
            print("Computer not found.")

    def osUpdate(self, computer, newOS):
        if computer in self.inventory:
            computer.operating_system = newOS
        else:
            print("Computer not found.")

    def refurbishComputer(self, computer, newOS):
        if computer in self.inventory:
            if int(computer.year) < 2000:
                computer.price = 0
            elif int(computer.year) < 2012:
                computer.price = 250
            elif int(computer.year) < 2018:
                computer.price = 550
            else:
                computer.price = 1000
            if newOS is not None:
                computer.operating_system = newOS
        else:
            print("Computer not found.")
        
    #for every computer in the inventory, pull information --> print information
    #else, print that that information isn't available
    # What methods will you need?