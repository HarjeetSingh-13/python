g=10
def display():
    global g
    g=50
    print(g)
def modify():
    global g
    g=g*2
print(g)
display()
print(g)
modify()
print(g)
