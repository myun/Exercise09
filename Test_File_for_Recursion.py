import recursion

number_list = [1,2,3,4,5]
print "When multiplying all the elements in the list", number_list, "the answer is", recursion.multiply_list(number_list)

n = 5
print "The factorial of", n, "is", recursion.factorial(n)


short_list = [0,1,2,3,4,5,6,7,8,9,10]
print "In the list", short_list, "there are/is", recursion.count_list(short_list), "element(s)."

list_to_add = [0,1,2,3,4,5]
print "The sum of the list", list_to_add, "is", recursion.sum_list(list_to_add) 

list_to_reverse = [9,8,7,6,5,4,3,2,1]
print "The reverse of", list_to_reverse, "is", recursion.reverse(list_to_reverse)

x = 10
print "The", x, "th Fibonacci number is", recursion.fibonacci(x)

list_to_search = [6,7,8]
element = 8
print "I will attempt to find the element", element, "in the list", list_to_search, "."
print "If found, I will return the element; otherwise I will print 'None'."
print "Result:", recursion.find(list_to_search, element)


def isPalindrome(word):
    if recursion.palindrome(word):
        print "The word", word, "is a palindrome!"
    else:
        print "The word", word, "is not a palindrome."

isPalindrome("racecar")
isPalindrome("lucky")

folds = 5
width = 8.5
height = 11
print "After", folds, "folds on a ", width, "by", height, "sheet of paper, the size of the paper is", recursion.fold_paper(width,height,folds)


target = 10
print "Counting up from 0 to a target of ", target, ":"
print recursion.count_up(target, 0)
