a= int(input('enter the marks'))
if a<25:
    print('F')
elif 25<=a<45:
    print('E')
elif 45<=a<50:
    print('D')
elif 50<=a<60:
    print('C')
elif 60<=a<80:
    print('B')
elif 80<=a<=100:
    print('A')
else:
    print('Invalid marks')
