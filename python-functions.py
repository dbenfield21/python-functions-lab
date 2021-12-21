import math 

# Challenge 1
# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# Example:
# sum_to(6)  # returns 21
# sum_to(10) # returns 55

num = int(input("Enter a number: "))
def sum_to(n):
    if n <= 1:
        return n
    else:
        return n + sum_to(n-1)
print("The sum equals: ", sum_to(num))

# Challenge 2
# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

# Example:
# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231



# num = int(input("Enter a list of 5 numbers"))
# def largest(n):
#     largest = 0
#     for x in n:
#         largest = x
#     else:
#         return largest
    
    # I cant make this work with a user inputting numbers... 


list_of_num = [5, 7, 26, 59, 75, 201]
def largest(list_of_num):
    return max(list_of_num)

print(largest(list_of_num))


# Challenge 3
# Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# Example:
# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0


def occurances (string1, string2):
    count = string1.count(string2)
    return count 

# test
# print(occurances("Bumblee Bee Buzzing", "B"))



# Challenge 4
# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

# Example:
# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0


def product (*args):
    product = 1
    for arg in args:
        product *= arg
    return product 

#test
# print (product(2, 7))
# print (product(9, 9, 1))