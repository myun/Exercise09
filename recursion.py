# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[len(l)-1] * multiply_list(l[:-1])

print multiply_list([1,2,3,4])

# Return the factorial of n
def factorial(n):
    total = 1
    if n == 1:
        return 1
    else:
        total = factorial(n-1) * n
    return total

print factorial(5)

# Count the number of elements in the list l
def count_list(l):
    if len(l) == 1:
        return 1
    else:
        return count_list(l[:-1]) + 1

print count_list([10,20,30,40,50])

# Sum all of the elements in a list
def sum_list(l):
    counter = 0
    if len(l) == 1:
        return l[0]
    else:
        counter = sum_list(l[:-1]) + l[-1]
    return counter

print sum_list([1, 2])

# Reverse a list without slicing or loops
def reverse(l):
    new_list = []
    if len(l) == 1:
        new_list.append(l[0])
        return new_list
    else:
        new_list.append(l.pop())
        reverse(l)
        print new_list
    return new_list


print reverse([1,2,3,4,5])
# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    pass

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    return None

# Determines if a string is a palindrome
def palindrome(some_string):
    return False

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    return (0, 0)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    return
