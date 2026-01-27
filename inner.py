def outer():
    print("this is outer ")
    def inner(a):
        print("this is inner ",a)
    return inner
something=outer()
something(5)


# something=outer()
# something()






# def inner(num):
#     print("this is inner ",num)
#     return inner
# something2=inner()
# something2(5)