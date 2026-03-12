x = 5   # global

def fun():
    y = 10   # local
    print(x) # can use global
    print(y)

fun()
print(x)   # works
print(y)   # error: y only existed inside fun()

#1--> Start with a local variable.
#2--> Is it inside any outer (parent) function?
#3--> Is it a global variable?
#4--> Is it a built in function?

def outer():
    x = 5
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)

outer()  
