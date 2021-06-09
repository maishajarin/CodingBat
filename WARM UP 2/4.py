def string_splosion(str):

    a=''
    for i in range(1, len (str)+1,1 ):
        for k in range(i):
            a+=str[k]
    return a