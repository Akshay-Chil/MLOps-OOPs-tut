# # Initiate a class
# class Employee():
#     # special method/magic method/dunder method - constructor
#     def __init__(self, ):
#         print(id(self))
#         # print("Started executing attributes")
#         self.id = 123
#         self.salary = 50000 
#         self.designation = "SDE"
#         # print("attributes have been initiated.")

#     def travel(self):
#         print("This function was called manually")
#         print("I love to travel to Nainital, Uttarakhand.")

# sam = Employee()
# sam.name = 'Akshay'
# print(sam.name)
# # shakti = Employee()
# # print(id(sam))
# # print(id(shakti))

# # sam.travel()
# # print(sam.designation)
# # print(sam.salary)
# # sam.travel()


# # print(type(sam))




###############################################################
#####################################################################

# class Employee():
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = first + "." + last + "@email.com"

#     def fullname(self):
#         return f'{self.first} {self.last}'
    
#     # def email(self):
#     #     return self.first + "." + self.last + "@email.com"

# emp_1 = Employee('Akshay', 'Chilwal')

# emp_1.first = 'Akku'
# print(emp_1.first)
# print(emp_1.last)
# # print(emp_1._Employee__email)
# print(emp_1.email)
# print(emp_1.fullname())


class person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def set_age(self, years):
        if years >= 0:
            self.__age += years
        else:
            print('Enter the valid year')

p1 = person('Akshay', 25)
print(p1.get_name())
print(p1.get_age())
p1.set_age(1)
print(p1.get_age())