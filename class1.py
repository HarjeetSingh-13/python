class employee:
    def display(self):
        print(self.name)
    def __init__(self):
        print('Object is created')
    def setname(self,n):
        self.name=n
e1=employee()
e2=employee()
e1.name='abc'
e1.display()
e1.setname('xy')
e1.display()
