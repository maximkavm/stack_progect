def rfs(str1,str2 =''):
    if str1 == '':
        return str2
    else:
        str2 += str1[-1]
        return rfs(str1[:-1], str2)




str5 = 'привет медвед'
print(rfs(str5))
