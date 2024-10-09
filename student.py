class Student:
     def __init__(self,name , house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Dragon","Ace","Ventura","Julia"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
            return f"{self.name} from {self.house}"

    def charm(self):
            if self.patronus == "St-Jean":
                return "Js"
            elif self.patronus == "ST-Jacques":
                return "SJ"
            elif self.patronus == "Majeur":
                return "Mineur"

def main():
    student = get_student()
    print (student)

def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return Student(name, house)

