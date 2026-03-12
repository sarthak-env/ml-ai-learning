some_list = ['a','b','c','b','d','m','n','n']
duplicates_list = []
seen = set()

for item in some_list[:]:           
    if item in seen:
        some_list.remove(item)      
        duplicates_list.append(item)
    else:
        seen.add(item)

print("Updated list:", some_list)
print("Duplicates:", duplicates_list)
