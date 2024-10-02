class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def display(self):
        print(f'ID: {self.id}\nName: {self.name}')
        
        
emp = Employee(1, "coder")

try:
    emp.display()
except:
    print("emp not exist")

