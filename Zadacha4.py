# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
#Как убрать магическое число 6?
S=int(input("Введите количество журавликов, кратное 6"))
if S<0:
    print("Не может количество журавликов быть отрицательным")
else:
    if S%6!=0:
        print("Полтора землекопа: не могут дети сложить долю от журавлика. Вводите кратное 6 число")
    else:
        a=S//6
        print(str(a)+str(4*a)+str(a))