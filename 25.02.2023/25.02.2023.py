# Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

# Используйте метод split строки. 
# a = input()
# s = a.split()
# sum = 0
# for i in range(len(s)):
#     sum=sum+int(s[i])
# print(sum)


# Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

# Если на вход пришло только одно число, надо вывести его же.

# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

# a = input()
# b = []
# a1 = a.split()
# sum = 0
# if len(a1) < 2:
#     b=a1
# else:
#     for i in range(len(a1)):    
#         if (i == 0):
#             sum = int(a1[i+1]) + int(a1[i-1])
#             b.extend([sum])   
#         elif (i == len(a1)-1):
#             sum = int(a1[i-1]) + int(a1[0])
#             b.extend([sum])
#         else:
#             sum = int(a1[i-1]) + int(a1[i+1])
#             b.extend([sum])            
# print(*b)


# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.

# Для решения задачи может пригодиться метод sort списка.

# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

a = input()
b = []
a1 = a.split()
j=1
for i in range(len(a1)):    
    if (a1[i] == a1[j]):
        if a1[i] in b:
            j+=1
            continue
                
        else:
                
            b.extend([a1[i]])  
            j+=1 
    else:
        j+=1
        continue
            
                   
print(*b)