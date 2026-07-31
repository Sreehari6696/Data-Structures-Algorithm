# This code is used to check if a number if a palindrom number or not using slicing method
# Example 1: Input = 121  ->  Output =   Entered number is Palindrome number 
# Example 2: Input = 123  ->  Output =   The entered number is not a palindrome number

N = int(input("Enter the number to be checked\n"))
n = str(N)
print("Entered number is Palindrome number " if n==n[::-1] else "The entered number is not a palindrome number")
