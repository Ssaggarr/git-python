
a=10 #global variable
def something():
    print(globals()['a']) #accessing global variable to local
    a=20 #local variable
    print("inside: ",a)
something()
print("outside ",a)
