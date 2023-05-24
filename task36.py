# Задача 36:
# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# (('house', 'дом'), ('car','машина'), ('men', 'человек'), ('tree', 'дерево'))
print("Введите строку в формате: ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N   ")
key_name=str(input(" "))
changed_key_name=key_name.replace( "="," ")
key_name_list=changed_key_name.split()
count=len(key_name_list)
first_list=[]
second_list=[]

i=0
while i<count:
    first_list.append(key_name_list[i])
    i+=2

i=1
while i<count:
    second_list.append(key_name_list[i])
    i+=2

data = list(zip(first_list, second_list))

print(data)