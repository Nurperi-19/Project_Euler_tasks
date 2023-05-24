#4) A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
lst = []
for i in range(100,1000):
    for y in range(100,1000):
        c=i*y
        if str(c)[0]==str(c)[-1] and str(c)[1]==str(c)[-2] and str(c)[2]==str(c)[-3]:
            lst.append(c)
print(max(lst))
