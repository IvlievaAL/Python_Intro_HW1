# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
n=int(input("Введите длину плитки в дольках: "))
m=int(input("Введите ширину плитки в дольках: "))
if n<=0 or m<=0:
    print("Шоколадка измеряется в натуральных числах")
else:
    k=int(input("Введите количество долек, которое нужно отломить от плитки: "))
    if k>n*m:
        print("Столько долек в шоколадке нет")
    elif k==n*m:
        print("Не надо ничего ломать, бери шоколадку целиком")
    else:
        if (k%n)==0 or (k%m)==0:
            print("Можно столько отломить")
        else:
            print("Нельзя столько отломить")