
def roman_to_int(s:str)->int:
    result=0
    a={'CM':900, 'CD':400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV':4,
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for k in a:
        result+=a[k]*s.count(k)
        s=s.replace(k, '')
    return result

def int_to_roman(num:int)->str:
    inform=['I', 'X', 'C', 'M']
    #      0    1    2    3   
    strange_number=''# 58 LVIII XXXXXIIIIIIII
    i=0
    while num != 0:
        n=num%10
        strange_number=inform[i]*n+strange_number
        num//=10
        i+=1
    result=strange_number
    result=result.replace('IIIIIIIII','IX')
    result=result.replace('IIIII', 'V')
    result=result.replace('IIII', 'IV')
    result=result.replace('XXXXXXXXX','XC')
    result=result.replace('XXXXX','L')
    result=result.replace('XXXX','XL')
    result=result.replace('CCCCCCCCC','CM')
    result=result.replace('CCCCC','D')
    result=result.replace('CCCC','CD')
    return result


