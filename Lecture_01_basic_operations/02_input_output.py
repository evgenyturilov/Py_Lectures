# ввод/вывод данных

print('Введите а')
a = input()
print('Введите b')
b = input()
print(a, b)
print('{} -- {}'.format(a, b))
c = a + b
print(a, ' + ', b, ' = ', c)                # в данном случае интерпретатор воспринимает переменные как строковые данные
                                            # для получения переменных от пользователя в целочисленном формате следует
                                            # команду ввода задавать в следующем виде int(input())

print(f'{a} - {b} - {c}')                   # интерполяция используется в качестве замены строки №8
print(a, '-', b, '-', c)                    # менее предпочтительный способ вывода
print('{2} - {1} - {0}'.format(a, b, c))    # пожно менять порядок вывода переменных