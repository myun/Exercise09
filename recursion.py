# Multiply all the elements in a list
def multiply_list(l):
    popped_elem = l.pop()
    if len(l) == 0:
        return popped_elem
    else:
        return popped_elem * multiply_list(l)


# Return the factorial of n
def factorial(n):
    total = 1
    if n == 1:
        return 1
    else:
        total = factorial(n-1) * n
    return total


# Count the number of elements in the list l
def count_list(l):
    if len(l) == 1:
        return 1
    else:
        del l[-1]
        return count_list(l) + 1


# Sum all of the elements in a list
def sum_list(l):
    counter = 0
    popped_elem = l.pop()
    if len(l) == 0:
        return popped_elem
    else:
        counter = sum_list(l) + popped_elem
    return counter


# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 1:
        return l
    popped = l.pop()
    return [popped] + reverse(l)


# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(10)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    popped = l.pop()
    if popped == i:
        return popped
    elif len(l) == 0:
        return "Sorry, we have no %r" % i
    else:
        return find(l, i)


print find([1,2,3,4,5,6,7], '8')

# Determines if a string is a palindrome
def palindrome(some_string):
    lower_string = some_string.lower()
    if len(lower_string) <= 1:
        return True
    elif lower_string[-1] != lower_string[0]:
        return False
    else:
        return palindrome(lower_string[1:-1])


# Given the width and height of a sheet of paper, and the number of times to fold it, 
# return the final dimensions of the sheet as a tuple. 
# Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    else:
        if width > height:
            return fold_paper(width/2.0, height, folds - 1)
        if width < height:
            return fold_paper(width, height/2.0, folds - 1)

print fold_paper(8, 11, 2)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    print n
    if n < target:
        count_up(target, n + 1)