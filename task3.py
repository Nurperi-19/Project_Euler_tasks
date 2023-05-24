#3) The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
def prime(number): #prime(13195)
    primefactor = 1
    i = 2
    while i <=number/2: # 2 <= 6797.5
        if number%i==0: # 13195%2!=0, 13195%3!=0, 13195%4!=0, 13195%5==0. 2639%2!=0, ... 2639%7==0 ...
            primefactor = i 
            number/=i   # 2639, 377, 29
        else:
            i+=1 # 2,3,4,6,8,9,10,11,12,14
    if primefactor < number: 
        primefactor = number
    return primefactor
print(prime(13195))
