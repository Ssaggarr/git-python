
def square(num):
    return num* num
def cube(num):
    return num*num*num
def operation(digits,choose):
    for i in digits:
        result=choose(i)
        print(result)
        
    # return choose(num) #square(num)or #cube(num)
digits=3,4,5
operation(digits,square)
