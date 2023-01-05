class person:
    def __init__(self):
        print('Consturctor is called')
    def display(self):
        print(self.name)
    def setname(self,n):
        self.name=n
    def setage(self,a):
        self.age=a

        
class student(person):#base class is person
    def __init__(self):
        print('Student is called')
    def setreg(self,reg):
        self.regist=reg
    def setroll(self,r):
        self.roll=r
  
class studentintern(student):
    def __init__(self):
        print('StudentIntern is called')
    def setwh(self,hrs):
        self.workhrs=hrs
    def setsalary(self,s):
        self.salary=s

        
a=person()
x=input('name ')
a.setname(x)
y=int(input('age '))
a.setage(y)
a.display()
b=student()
x=input('name ')
b.setname(x)
y=int(input('age '))
b.setage(y)
reg=int(input('reg '))
b.setreg(reg)
roll=int(input('roll '))
b.setroll(roll)
b.display()
c=studentintern()
x=input('name ')
c.setname(x)
y=int(input('age '))
c.setage(y)
reg=int(input('reg '))
c.setreg(reg)
roll=int(input('roll '))
c.setroll(roll)
hrs=int(input('work hours '))
c.setwh(hrs)
sal=int(input('salary'))
c.setsalary(sal)
c.display()

