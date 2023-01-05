def displaymenu():
    print('1. Mathematical functions')
    print('2. Play Game')
    print('3. Display Result')
    print('4. Exit')
    option=int(input('Enter your choice: '))
    return option
def mathsmenu():
    print('1. Power')
    print('2. Factorial')
    print('3. Log')
    print('4. Floor')
    moption=int(input('Enter your choice: '))
    if moption==1:
        a=int(input('Enter first value: '))
        b=int(input('Enter second value: '))
        print(a**b)
    elif moption==2:
        a=int(input('Enter a value: '))
        f=1
        for i in range(1,a+1):
            f*=i
        print(f)
    elif moption==3:
        print('log option not available at the moment')
    elif moption==4:
        a=float(input('Enter a value: '))
        print(floor(a))
    else: 
        print('Invalid input')
option=1
while option!=4:
    option=displaymenu()
    if option==1:
        moption=mathsmenu()
    elif option==2: 
        print('Modue 2')
    elif option==3:
        print('Module 3')