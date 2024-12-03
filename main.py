third=int(input('Введите любое число: '))   #firs, second, third
second=int(input('Введите любое число: '))
firs=int(input('Введите любое число: '))
if third==second and second==firs:
    print(3)
elif third==second or third==firs or second==firs:
    print(2)
elif not third==second and not second==firs and not second==firs:
    print(0)


