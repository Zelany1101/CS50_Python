class Student:
    def __init__(self, name, house):    #initialization of an object in python; self argument implies access to the current object just created; Automatically passes in a reference to an argument that represents the current object that the user just constructed in memory for the user.
        self.name = name                #adding instance variables to objects
        self.house = house


    def __str__(self):                  #takes one argument, self; called whenever converting student object to a string
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name :                   # same as if name == ""
            raise ValueError("Missing name")
        self._name = name

    @property #getter
    def house(self):
        return self._house

    @house.setter #setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)             #constructor call== line of code constructing an object using the
                                           #student class as a template so every object is structure the same

if __name__ == "__main__":
    main()
