import sys
from time import sleep
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())
count=1
def recur():
    global count
    print("completed ",count)
    count=count+1
    sleep(0.5)
    recur()
recur()




#factorial using recursion
def fact(num):
    if num==1:
        return 1
    return num * fact(num-1)
result=fact(5)
print(result)
    