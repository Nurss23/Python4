nums = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    15:'fifteen',
    18:'eighteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
}

def gen_num(n,dct):
    tmp = ''
    t = str(n)

    if dct.get(n,False): #
        return dct[n]
    elif n < 20:
        return dct[int(t[1])]+'teen'
    elif n < 100:
        tmp = n - int(t[1])
        return dct[tmp]+dct[int(t[1])]
    elif n < 1000:
        if t [1:3] == '00':
            return dct[int(t[0])] + 'hundred'
        else:
            return dct[int(t[0])] + 'hundredand' + gen_num(int(t[1:3]),nums)
    elif n == 1000:
        return 'onethousand'

s = 0
for i in range(1,1001):
    s += len(gen_num(i,nums))
print(s)
