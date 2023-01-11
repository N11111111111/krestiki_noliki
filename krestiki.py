
print("Игра крестики - нолики")

def out_red(text):
    print("\033[34m{}".format(text))

Pole = [["-"] * 3 for _ in range(3)]
def show_Pole(f):
    print('  0 1 2')
    for i in range(len(Pole)):  # распаковали и вывели построчно
        print(str(i), *Pole[i])
#show_Pole(Pole)

def opros(f):
    while True:
        zif = input("Ведите координаты через пробел").split()
        if len(zif) != 2:
            print("Вы ввели не две координаты")
            continue
        if not(zif[0].isdigit() and zif[1].isdigit()):
            print("Координаты должны быть цифрами")
            continue
        x,y = map(int,zif)
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print("Введенные координаты не соответствуют диапазону")
            continue
        if f[x][y] != "-":
            print("Клетка занята")
            continue
        break

    return x,y

def proverka(f, user):
    def proverka_linii(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
             return  True
    for n in range(3):
        if proverka_linii(f[n][0], f[n][1], f[n][2], user) or \
        proverka_linii(f[0][n], f[1][n], f[2][n], user) or \
        proverka_linii(f[0][0], f[1][1], f[2][2], user) or \
        proverka_linii(f[2][0], f[1][1], f[0][2], user):
            return True
    return False

 #opros(Pole)
count = 0
while True:
    if count % 2 == 0:
        user = "х"
    else:
        user = "0"
    show_Pole(Pole)
    x,y = opros(Pole)
    Pole[x][y] = user
    if count == 9:
        print("Ничья!")
    if proverka(Pole, user):
        show_Pole(Pole)
        out_red (f"Поздравляем! Выиграл {user}!")
        break
    count+=1


