picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
def trees():
    for row in picture:
        for pixel in row:
            if (pixel==0):
                print(' ',end='')
            else:
                print('*',end="")
        print('')

trees()
trees()
trees()

#Parameters
def say_hello(name, emoji):
    print(f"Hey {name}, how are you today?{emoji}")

#Arguments
say_hello("Sarthak",'😊')

#Default Parameters
def say_hello(name='User', emoji='🙏'):
    print(f"Hey {name}, how are you today?{emoji}")

say_hello()
say_hello("Sarthak",'😊')

# return: Sends back the data.
def add(a,b):
    return a+b

total=add(5,6)
print(add(total,2))