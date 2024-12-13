from random import *
from math import pow, log2


# Функция для безопасного возведения в степень по модулю
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod  # Приводим основание к модулю, чтобы не было переполнения
    while exp > 0:
        # Если степень нечётная, умножаем на текущий результат
        if exp % 2 == 1:
            result = (result * base) % mod
        # Умножаем основание на себя для следующей степени
        base = (base * base) % mod
        exp = exp // 2  # Делим степень пополам
    return result

#генератор для случайного num-2>=a>=2
def AGenerator(num):
    a=randint(2,num-2)
    return a

#генератор числа, если входные данные это разряд числа
def NumGenerator(raz):
    num=randint(int(pow(10,raz-1)), int(pow(10,raz)-1))
    return num

#алгоритм Евклида для нахождения НОД (наибольший общий делитель)
def EuclidAlghoritm(num1,num2):
    NOD=0
    while True:
        num=max(num1,num2)
        if num ==num1:
            num1%=num2
        else:
            num2%=num1
        if num1==0:
            NOD=num2
            break
        elif num2==0:
            NOD=num1
            break
    return NOD

#Тест Рабина-Миллера для проверки на то, что число простое
def MillerRabinTest(num,k):
    if num <= 0:
        return False  # Числа <= 0 не являются простыми
    if num == 2 or num == 3:
        return True  # 2 и 3 — простые числа
    if num % 2 == 0:
        return False  # Четные числа не являются простыми

    #шаг 2 (формула n-1=2^s * t) находим s и t
    n_1=num-1
    t=0
    s=0
    while True:
        if n_1%2==0:
            n_1//=2
            s+=1
        else:
            t=n_1
            break
    a_mas=[]
    for i in range(k):
        a=1
        while a not in a_mas:
            a=AGenerator(num)
            if a not in a_mas:
                a_mas.append(a)
                break

            #шаг 1 по алгоритму Евклида находим НОД среди случайного числа 1<a<num и num 
        NOD=EuclidAlghoritm(a,num)
        if NOD != 1:
            return False
        try:
            x=mod_exp(a,t, num)
            if x == 1 or x == num-1:
                continue
        except OverflowError:
            continue
        for j in range(1,s):
            x=mod_exp(a,2, num)
            if x==1:
                return False
            elif x==num-1:
                break
            elif j==s-1:
                return False
    return True

def RunnigCode(raz):
    num=NumGenerator(raz)
    k=100
    # k=10000
    return num, MillerRabinTest(num,k)

a=MillerRabinTest(17, 1)
if a is True:
    print("простое")
else:
    print("составное")

# evid=0
# while evid is not True:
#     num,evid = RunnigCode(5)
#     if evid is True:
#         print(f"{num}  простое")
#     else:
#         print(f"{num}  составное")

