# Store a string in a variable
quote = '"To be or not to be"'
print(quote)  
# Prints: "To be or not to be"

# 1) len(): Returns the length (number of characters in the string)
print(len(quote)) 
 # 18 characters (includes spaces and quotes)

# 2) upper(): Converts the entire string to uppercase
print(quote.upper()) 
 # "TO BE OR NOT TO BE"

# 3) capitalize(): Capitalizes the first character of the string
print(quote.capitalize())  
# "To be or not to be"

# 4) find(): Returns the index of the first occurrence of a substring
print(quote.find('be'))  
# 4 (index starts at 0)

# 5) replace(): Replaces all occurrences of a substring with another
print(quote.replace('be', 'me'))  
# "To me or not to me"
