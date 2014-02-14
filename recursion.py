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
    if len(l) == 1:
        return l
    popped = l.pop()
    return [popped] + reverse(l)

print reverse([1,2,3,4,5])

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    #Come back to fill out base case
    if n == 1 or n == 0:
        return n
    else:
        n = fibonacci(n-1) + fibonacci(n-2)
        return n
#it works and I want to eat small children now. Thanks, Fibonacci! :)
print fibonacci(10)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    popped = l.pop()
    if popped == i:
        return popped
    elif len(l) == 0:
        #FLAMES!!!
        return "Sorry, we have no %r" % i
    else:
        return find(l, i)


print find([1,2,3,4,5,6,7], 'bananas')

# Determines if a string is a palindrome
def palindrome(some_string):
#I have no idea how we did this, but IT WORKS!
    some_list = some_string.split()
    some_letter = some_list.pop()
    if len(some_list) == 0:
        return True
    elif some_letter == some_list[0]:
        del some_list[0]
        palindrome(some_list)
    else:
        return False

print palindrome("mom")

# Given the width and height of a sheet of paper, and the number of times to fold it, 
#return the final dimensions of the sheet as a tuple. 
#Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    return (0, 0)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    return
    #look at factorial
    # use another variable
    #nap. 