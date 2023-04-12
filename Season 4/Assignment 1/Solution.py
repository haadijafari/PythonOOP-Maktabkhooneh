class Person:
    def __init__(self, name:str(), age:int()):
        self.name = name.title()
        self.age = age
        
    def display(self):
        print(f'{self.name} -->\nAge: {self.age}')
        
class Student(Person):
    def __init__(self, name:str(), age:int(), major:str()):
        super().__init__(name, age)
        self.major = major.title()
    
    def displayStudent(self):
        super().display()
        print(f'Major: {self.major}')
        
if __name__ == '__main__':
    stu1 = Student('hadi', 20, 'computer science')
    stu1.displayStudent()