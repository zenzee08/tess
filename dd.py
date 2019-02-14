print ('program untuk menentukan bilangan terbesar ')

def pengulangan():
    print ('masukkan 3 bilangan yang diinginkan!')
    a=int(input('bilangan1 = '))
    b=int(input('bilangan2 = '))
    c=int(input('bilangan3 = '))

    if a>b and a>c:
        if b>c:
            print (a, 'terbesar dari 3 bilangan yang di input')
        else:
            print (a, 'terbesar dari 3 bilangan yang di input')
    elif b>a and b>c:
        if a>c:
            print (b, 'terbesar dari 3 bilangan yang di input')
        else:
            print (b, 'terbesar ddari 3 bilangan yang di input')
    else:
        if a>b:
            print (c, 'terbesar dari 3 bilangan yang di input')
        else:
            print (c, 'terbesar dari 3 bilangan yang di input')

    print ('')
    print ('ingin coba lagi? (ya/tidak)')
    x=input()
    if x=='ya':
        return pengulangan()
    if x=='tidak':
        print('..')

pengulangan()
