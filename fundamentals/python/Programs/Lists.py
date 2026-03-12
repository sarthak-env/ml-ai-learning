amazon_cart=['bagpacks',
             'laptops',
             'books',
             'electronics',
             'watches',
             'stationary']

print(amazon_cart[0])

'''
    List Slicing: Works similar to the string slicing.

    Syntax: var_name[start:stop:stepover]

    Note: Strings are immutable but the lists are mutable(You can change value of an object at a certian index)
'''
amazon_cart[2]='games'
print(amazon_cart)
     