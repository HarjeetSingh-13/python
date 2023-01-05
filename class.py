class Employee:
    def _init_(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def call(self):
        print('Name:',self.name)
        print('age:', self.age)
        print('salary:', self.salary)

name=input('Enter employee name: ')
age=int(input('Enter employee age: '))
salary=int(input('Enter employee salary: '))
Emp_1 = Employee()
Emp_1.name,Emp_1.age,Emp_1.salary=name,age,salary
Emp_1.call()
