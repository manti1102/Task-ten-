#Нахождение наименьшего числа:
#Программа принимает три целых числа от пользователя и выводит значение наименьшего из них

number1 = int(input("Введите число"))
number2 = int(input("Введите число"))
number3 = int(input("Введите число"))
if number2 >= number1 <= number3:
    print(number1)
elif number1 >= number2 <= number3:
    print(number2)
else:
    print(number3)