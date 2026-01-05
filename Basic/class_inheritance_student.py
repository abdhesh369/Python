class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def great(self):
        print(f"Hi, I am {self.name}")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def Study(self):
        print(f"I am studying grade {self.grade}")


a=Student("Abdhesh",22,"Bechlor")    
a.great() 
a.Study()           