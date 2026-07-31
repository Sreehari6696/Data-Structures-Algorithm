# This code is used to check whether two strings are anagram or not
# Example 1: Input  string1 = anagram,  string2 = nagaram    ->    Output =  "The entered strings are anagram"
# Example 2: Input  string1 = anagram,  string2 = nagaramm   ->    Output =  "The entered strings are not anagram"
s1 = input("Enter the first string\n")
s2 = input("Enter the second string\n")
d1={}
d2={}
for i in s1:
    d1[i] = s1.count(i)
for j in s2:
    d2[j] = s2.count(j)
print("The entered strings are anagram" if d1==d2  else "The entered strings are not anagram")
