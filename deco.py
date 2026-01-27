# #DECORATORS
# def greater(func):
#     def wrap(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return wrap
    
def log(func):
    def wrap(*args):
        print("values ",args)
        result=func(*args)
        print("result",result)
        return result
    return wrap



# @greater #one way of doing it
# @log
# def sub(a,b):
#     # if a<b:
#     #     a,b=b,a
#     return a-b
# # result=sub(2,5)
# # print(result)
# @log
# @greater
# def div(a,b):
#      return a/b
# # result2=div(10,3)
# # print(result2)


# # sub=greater(sub)
# # div=greater(div) #another way of doing it but this part should be in between def and result

# result2=div(10,3)
# print(result2)

# result=sub(5,2)
# print(result)


        



@log        
def bigfirst(*args):
    return args
result3=sum(bigfirst(300,200,500,600))
print(result3)
