# Initiate a class
class Employee():
    # special method/magic method/dunder method - constructor
    def __init__(self, ):
        print("Started executing attributes")
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
        print("attributes have been initiated.")

    def travel(self):
        print("This function was called manually")
        print("I love to travel to Nainital, Uttarakhand.")

sam = Employee()

# print(sam.designation)
# print(sam.salary)
sam.travel()


print(type(sam))


lst = [1, 2, 3]
print(type(lst))