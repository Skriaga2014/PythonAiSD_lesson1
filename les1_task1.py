'''
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

a = int(input('Введите трехзначное число: '))
a1 = a//100
a2 = a%100//10
a3 = a%10
summ = a1+a2+a3
proizv = a1*a2*a3
print('Сумма:       ', summ)
print('Произведение:', proizv)
#