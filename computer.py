class Computer:
    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    price: int
    year: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
   
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, price, year):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.price = price
        self.year = year
    # What methods will you need?
    def printDetails(self):
        print(self.description)
        print(self.processor_type)
        print(self.hard_drive_capacity)
        print(self.memory)
        print(self.operating_system)
        print(self.price)
        print(self.year)

def main():
    myComputer = Computer("Mac Pro", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "MacOS Monterey", 550, 2013)
    myComputer.printDetails()

main()

