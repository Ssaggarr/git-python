# #variable length aruments

# def sagar(num1,*num2):
    
#     total=num1
#     for n in num2:
#         total=total+n
#     return(total)
# print(sagar(20,30,40,50))

#default  arguments

# def sagar(num1=0,num2=0):
    
#     total=num1+num2
    
#     return(total)
# print(sagar())

#keyword arguments
# def person(age,name):
    
#     print('name : ',name )
#     print('age : ',age )
    
# person(name='sagar',age=21)

#keyword length arguments
def person(name,**kwlargs):
    
    print('name : ',name )
    print('dict : ',kwlargs)
    for k,v in kwlargs.items():
        print(k," : ",v)
        
person(name='sagar',age=21,loc='bangalore',gender='male')
