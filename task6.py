num = int(input("Введите шестизначное число: "))
while num < 100000 or num > 999999:
    num = int(input(f'''Вы ввели не шестизначное число
    Введите шестизначное число: '''))

bilet = list(str(num))
first_three = int(bilet[0]) + int(bilet[1]) + int(bilet[2])
second_three = int(bilet[3]) + int(bilet[4]) + int(bilet[5])

print(f"{num} >>> yes" if first_three == second_three else f"{num} >>> no")