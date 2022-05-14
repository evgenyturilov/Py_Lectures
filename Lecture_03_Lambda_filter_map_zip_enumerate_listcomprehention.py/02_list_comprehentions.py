# Задача - составить список, состоящий из четных элементов:

# Алгоритмический способ решения задачи:

list = []

for i in range(1,21):
    if(i%2 == 0):
        list.append(i)
print(list)

# При помощи list comprehention это делается следующим образом:

list = [i for i in range(1,21) if i%2 == 0]
print(list)

# Можно получать список кортежей:

list = [(i, i) for i in range(1,21) if i%2 == 0]
print(list)

# Можно обрабатывать данные:

def f(x):
    return x**3

list = [f(i) for i in range(1,21) if i%2 == 0]
print(list)

list = [(i, f(i)) for i in range(1,21) if i%2 == 0]
print(list)