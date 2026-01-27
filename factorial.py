
def fact(num):
    useless=1
    for i in range(1,num+1):
        useless=useless*i
    return useless

result=fact(5)
print(result)