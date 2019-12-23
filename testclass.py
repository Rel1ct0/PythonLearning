#!/usr/bin/python3

class Testclass():
    def __init__(self, first, second, optional=''):
        self.name = first
        self.surname = second
        self.middlename = optional

    def printme(self):
        print("Name is " + self.name.title())
        print("Surname is " + self.surname.title())
        if (self.middlename):
            print("Middlename is " + self.middlename.title())


class Child(Testclass):
    def __init__(self, first, second, optional='', victims=0):
        super().__init__(first, second, optional)
        self.victims = str(victims)
    
    def printme(self):
        super().printme();
        print(self.victims)


ziga = Testclass("Adolf", "Hitler", "Alibabaevich")
ziga.printme()
print(ziga.name)

zaga = Child("Alexey" , "Navalniy", "Batkovich", 10000)
zaga.printme()
