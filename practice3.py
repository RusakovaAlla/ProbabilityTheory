from math import factorial, sqrt
import numpy as np
import pandas as pd

def combos(n, k):
    """
    :param n: из какого числа делаем выборку
    :param k: сколько выбираем
    :return: число исходов
    """
    return factorial(n) / (factorial(k) * factorial(n - k))

#Задача1
"""Даны значения зарплат из выборки выпускников:
100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
Посчитать (желательно без использования статистических методов наподобие std, var, mean)
среднее арифметическое,
среднее квадратичное отклонение,
смещенную и несмещенную оценки дисперсий для данной выборки.
"""


def mean_arthm(some_array):
    mn_a = sum(some_array) / len(some_array)
    return mn_a


def disp(some_array, move=False):
    """
    :param some_array: массив
    :param move: для оценки дисперсии, move=True - смещенная, False - несмещенная
    :return:оценка дисперсии
    """
    meanArthm = mean_arthm(some_array)
    mean_arr = [(i - meanArthm) ** 2 for i in some_array]
    if move:
        s = sum(mean_arr)/(len(mean_arr)-1)
    else:
        s = sum(mean_arr)/len(mean_arr)

    return s


def array_descr(some_array):
    """
    :param some_array:
    :return:
    """
    meanArthm = mean_arthm(some_array)
    sko = sqrt(sum([(i - meanArthm)**2 for i in some_array])/len(some_array))
    s_moved = disp(some_array, move=False)
    s_unmoved = disp(some_array, move=True)
    print(f"Среднее арифметическое: {meanArthm} \n"
          f"Cреднее квадратичное отклонение: {round(sko, 2)} \n"
          f"Cмещенная оценка дисперсии для выборки: {round(s_moved, 2)} \n"
          f"Несмещенная оценка дисперсии для выборки: {round(s_unmoved, 2)} ")

    return meanArthm, sko, s_moved, s_unmoved

arr = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
print(f"{'_'*10}Ответ к Задаче 1{'_'*10}")
descr = array_descr(arr)
print()


#Задача2
"""В первом ящике находится 8 мячей, из которых 5 - белые. 
Во втором ящике - 12 мячей, из которых 5 белых. 
Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?
"""
w21 = combos(5, 2)*combos(3,0)/combos(8,2)*combos(5,1)*combos(7, 3)/combos(12, 4)
w12 = combos(5, 1)*combos(3,1)/combos(8,2)*combos(5,2)*combos(7, 2)/combos(12, 4)
w03 = combos(5, 0)*combos(3,2)/combos(8,2)*combos(5,3)*combos(7, 1)/combos(12, 4)
p = (w21+w12+w03)*100
print(f"{'_'*10}Ответ к Задаче 2{'_'*10}")
print(f"вероятность того, что 3 мяча белые - {round(p, 2)}%")
print()

#Задача3
"""На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
Найти вероятность того, что выстрел произведен: 
a). первым спортсменом 
б). вторым спортсменом 
в). третьим спортсменом.
"""
accuracy = np.array([0.9, 0.8, 0.6])
p = sum(accuracy*1/3) #полная веростность
acc_prob = [i*1/3/p*100 for i in accuracy]
print(f"{'_' * 10}Ответ к Задаче 3{'_' * 10}")
[print(f"Вероятность того, что мишень попал {num+1} спортсмен - {round(i, 2)}%", end="\n")
 for num, i in enumerate(acc_prob)]
print()


#Задача4
"""В университет на факультеты A и B поступило равное количество студентов, 
а на факультет C студентов поступило столько же, сколько на A и B вместе. 
Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию. 
Какова вероятность, что он учится: 
a). на факультете A 
б). на факультете B 
в). на факультете C?
"""
students_data = pd.DataFrame({"Pass_Prob": [0.8, 0.7, 0.9]}, index=["A", "B", "C"])
#пусть x - количество студентов, поступивших на факультеты A и B
#Тогда всего поступило студентов: x+x+2x = 4x
#Условно примем за 1 количество всех учащихся и найдем x, как долю учащихся на факультетах A и B
# 1 = 4x => x = 0.25
#x = 0.25 #т.к. на факультете С учится в 2 раза больше студентов, то вероятность - 0.25*2 = 0.5
students_data["student2faculty"] = [0.25, 0.25, 0.5]
pass_exam = sum(students_data["student2faculty"]*students_data["Pass_Prob"])#полная вероятность сдать сессию
students_data["Prob_Pass_Student"] = students_data["student2faculty"]*students_data["Pass_Prob"]/pass_exam*100
print(f"{'_' * 10}Ответ к Задаче 4{'_' * 10}")
[print(f"Вероятность того, что сессию сдал студент факультета {students_data.index[num]} - {round(i, 2)}%", end="\n")
 for num, i in enumerate(students_data['Prob_Pass_Student'])]
print()

#Задача5
"""Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, 
для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя: 
а). все детали 
б). только две детали 
в). хотя бы одна деталь 
г). от одной до двух деталей?
"""
p_a = 0.1*0.2*0.25
p_b = 0.1*0.2*0.75+0.1*0.25*0.8+0.9*0.2*0.25
p_v = 1-0.9*0.8*0.75
p_g = 1-p_a-p_b-p_v#т.к. взаимоисключающие
print(f"{'_' * 10}Ответ к Задаче 5{'_' * 10}")
print(f"Вероятность того, что в первый месяц выйдут из строя все детали равна {round(p_a, 2)*100}%")
print(f"Вероятность того, что в первый месяц выйдут из строя только две детали {round(p_b, 2)*100}%")
print(f"Вероятность того, что в первый месяц выйдут из строя хотя бы одна деталь {round(p_v, 2)*100}%")
print(f"Вероятность того, что в первый месяц выйдут из строя от одной до двух деталей {round(p_g, 2)*100}%")
print()
