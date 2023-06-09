#2) Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.
result = []
def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
for i in range(80):
    if fib(i) > 4000000:
        break
    else:
        result.append(fib(i))
result = list(filter(lambda x: x%2==0, result))
print(sum(result))
