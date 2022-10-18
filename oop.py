class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


name = input("Enter name: ")
age = int(input("Enter age: "))
p1 = Person(name,age)
print(p1.name,p1.age)


