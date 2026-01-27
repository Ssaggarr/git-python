def add(a,b):
    store=a+b #this part is called expression which is main part in defining function
    return store


result=add(4,5)
print(result)

#this is normal procedure for defining fuction 
#when we want to do the same for anonymous function

add=lambda a,b :a+b #you can do that in one line itself where lambda in inbuilt anonymous function

result=add(4,5)
print(result)

#ANOTHER EXAMPLE
def square(a):
    store=a*a
    return store

#normal way above 
square=lambda a :a*a


result=square(5)
print(result)