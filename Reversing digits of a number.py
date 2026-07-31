# This is a code used for reversing the digits of a number. 
# If the original number has trailing zeros then our code would neglect them and proceed reversing the other digits.
# Example 1: input = 567    ->   output = 765
# Example 2: input = 190900 ->   output = 9091

N = int(input("Enter the number to be reversed\n"))
final=[]
n = list((str(N)[::-1]))
for i in range(len(n)):
    if n[i]=='0':
        continue
    else:
        for j in range(i,len(n)):
            final.append(n[j])
        break
print(''.join(final))
