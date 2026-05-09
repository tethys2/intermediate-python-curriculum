class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def introduce(self):
        print("Hi, my name is", self.name)
        print("I am in grade", self.grade)

student1 = Student("Aarav", 5)
student1.introduce()

student2 = Student("Rianna", 7)
student2.introduce()
