#17) If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used? Do not count spaces or hyphens. 

from0to19 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

def lst2(string):
    lstnum = list(map(lambda x: string+x, from0to19[:10]))
    return lstnum
num00 = from0to19 + lst2('twenty') + lst2('thirty') + lst2('forty') + lst2('fifty') + lst2('sixty') + lst2('seventy') + lst2('eighty') + lst2('ninety')

def lst3(string):
    num00
    lstnum3 = list(map(lambda x: string+'hundredand'+x, num00[1::]))
    lstnum3.insert(0, string+'hundred')
    return lstnum3
num000 = lst3('one') + lst3('two') + lst3('three') + lst3('four') + lst3('five') + lst3('six') + lst3('seven') + lst3('eight') + lst3('nine') 

num1000 = num00 + num000 + ['onethousand']
finalnums = (list(map(lambda x: len(x), num1000)))

while True:
    try:
        num = int(input('Number: '))+1
        result = finalnums[1:num]
        print(sum(result))
    except:
        print('Enter only numbers')
