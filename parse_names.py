# Exercise: parse names in a list.

# take a list of names
# remove duplicates
# title case the names
# sort alphbetical descending order by surname
# determine the shortest surname

names = 'sarah liver, jackie robinson, aria caro, bruce buffer, cliff manner, fred friedman, aria caro'
name_list = set((names.split(', '))) # Make a set to remove duplicates.
name_list = list(name_list) # Change to list for indexing and list comprehension.

# List comprehension - make new list with capital first letters.
cap_name_list = [x.title() for x in name_list]

cap_name_list.sort() # Sorts by first letter of first name.

def surname(name):
    """Returns surname for sorting instead of using the first name."""
    return(name.split(' ')[1])

cap_name_list.sort(reverse=True, key=surname) # sorts by surname by calling surname function.

print('This name list is sorted by surnames in reverse order: ')
print(cap_name_list)
print()



print(final_names)

