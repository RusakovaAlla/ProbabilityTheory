from math import factorial, e

#подготовим функцию
def combos(n, k):
    """
    :param n: из какого числа делаем выборку
    :param k: сколько выбираем
    :return: число исходов
    """
    return factorial(n) / (factorial(k) * factorial(n - k))


#Задача1
"""
Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
Стрелок выстрелил 100 раз.
Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
"""
P = combos(100, 85)*0.8**85*0.2**15*100
print(f"{'_'*10}Ответ к Задаче 1{'_'*10}")
print(f"Вероятность того, что стрелок попадет в цель ровно 85 раз составляет {round(P, 2)}%")
print()

#Задача2
"""Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?
"""
#т.к. вероятность наступления события очень мала, используем формулу распределения Пуассона
m = [0, 2] #список количества наступлений событий
n = 5000
l = 0.0004*5000

print(f"{'_'*10}Ответ к Задаче 2{'_'*10}")
for event in m:
    Pm = round(l**event/factorial(event)*e**(-l)*100, 2)
    print(f"Вероятность перегорания {event} лампочек составляет {Pm}%")
print()

#Задача3
"""
Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
"""
P = combos(144, 70)*0.5**70*0.5**74*100
print(f"{'_'*10}Ответ к Задаче 3{'_'*10}")
print(f"Вероятность, что орел выпадет ровно 70 раз {round(P, 2)}%")
print()

#Задача4
"""
В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых. 
Из каждого ящика вытаскивают случайным образом по два мяча. 
Какова вероятность того, что все мячи белые? 
Какова вероятность того, что ровно два мяча белые? 
Какова вероятность того, что хотя бы один мяч белый?
"""

print(f"{'_'*10}Ответы к Задаче 4{'_'*10}")
#ответ на первый вопрос найдем через условную вероятность
p = 7/10*6/9*9/11*8/10*100
print(f"Вероятность, что все мячи белые - {round(p, 2)}%")

#ответ на второй вопрос через условную вероятность
p_cond = 7/10*6/9*2/11*1/10+\
         7/10*3/9*9/11*2/10+\
         7/10*3/9*2/11*9/10+\
         3/10*2/9*9/11*8/10+\
         3/10*7/9*9/11*2/10+\
         3/10*7/9*2/11*9/10
p_cond *= 100
#ответ на второй вопрос сочетаниями
p20 = combos(7, 2)*combos(3, 0)/combos(10, 2)*combos(2, 2)*combos(9, 0)/combos(11, 2)
p02 = combos(7, 0)*combos(3, 2)/combos(10, 2)*combos(2, 0)*combos(9, 2)/combos(11, 2)
p11 = combos(7, 1)*combos(3, 1)/combos(10, 2)*combos(2, 1)*combos(9, 1)/combos(11, 2)
p = (p20+p02+p11)*100
print(f"Вероятность, что ровно два мяча белые - {round(p, 2)}% (или для решения через сочетания - {round(p_cond, 2)}%)")

#ответ на третий вопрос вопрос
#решаем от противного, ищем вероятность, что ни один мяч не будет белым
p = (1-3/10*2/9*2/11*1/10)*100

#решаем сочетаниями - доделать, но муторно
p_comb = combos(7, 0)*combos(3, 2)/combos(10, 2)*combos(2, 2)*combos(9, 0)/combos(11, 2)
print(f"Вероятность, что хотя бы один мяч белый - {round(p, 2)}% (или для решения через сочетания - "
      f"{round((1-p_comb)*100, 2)}%)")
