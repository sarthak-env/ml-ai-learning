
num_1= 20
num_2= 3.142
num_3= -45

'''
    1) round():-
        This is used to round of the values of the floating point
        Syntax: round(number,ndigit)
'''
print(round(num_2,1))
print(round(num_2,3))
print(round(num_2,5))

'''
    2) bin():-
        Returns binary number of the given number
        Syntax: bin(number)
'''
print(bin(num_1))

'''
    3) abs():-
        This returns the absolute value (positive value) of a given number
        Syntax: abs(number)
'''
print(abs(num_1))
print(abs(num_3))

'''
    4) Arithmatic Operations:-
'''
print(2+3) #Addition
print(4-2) #Substraction
print(4*9) #Multipllicatioon
print(4/2) #Division

'''
    5) Floating addition:-
'''
print(9.9+1.1)
#Keeps the decimall point even if thr value is whole (ie. 11.0 )


'''
    6) Exponential:-
'''
print(2**4)

'''
    7) Floor Division:-
        This rounds down the value to the nearest whole number towards negative infinity
'''
print(4//2)
# 0.5 is closer to zero than one here

'''
    8) Modulo operator:-
       Returns the remainder of the dividion
'''
print(10%4)

'''
    9) operator precedence:-
       ()
       **
       *,/
       +,-
       High to low precedence
'''
print(20-3*4)
print(20-(3*4))

'''
    10) Augmented assignment operator:-
       An augmented assignment operator is a shorthand way to combine an operation with assignment
'''
x=21
x += 5 # This is the augmented assignment operator.
print(x)



