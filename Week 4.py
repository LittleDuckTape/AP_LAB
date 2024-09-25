# First Function (union of lists):
def unify_lists(a, b):
    return list(set(a).union(set(b)))

# Example 1:
a = [1, 3, 5]
b = [1, 2, 3]
print(unify_lists(a, b)) # Output should be [1, 2, 3, 5]

# Example 2:
a = [2, 4, 6]
b = [2, 4, 6]
print(unify_lists(a, b)) # Output should be [2, 4, 6]

# Example 3:
a = [1, 2, 3, 4]
b = [4, 5, 6, 7]
print(unify_lists(a, b)) # Output should be [1, 2, 3, 4, 5, 6, 7]

#-----------------------------------------------

# Second Function (tuple, integers, and string):
def duplicate_char(num_elements, string_length):
    if len(num_elements) != len(string_length):
        raise ValueError("The number of elements in the tuple must equal the length of the string.")
    
    result = []
    
    for count, char in zip(num_elements, string_length):
        result.append(char*count)
    
    return ''.join(result)

# Example 1:
tuple = (1, 2, 3, 4)
str = 'alex'
print(duplicate_char(tuple, str)) # Output should be 'alleeexxxx'

# Example 2:
tuple = (1, 2, 1)
str = 'pan'
print(duplicate_char(tuple, str)) # Output should be 'paan'

# Example 3:
tuple = (5,)
str = 'z'
print(duplicate_char(tuple, str)) # Output should be 'zzzzz'