# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
def SumOfThreeDigits (i):
    count=0
    Sum=0
    while count<3:
        Sum=Sum+N%10^i//10^(i-1)
        count+=1
    return Sum
N=int(input ("Введите шестизначное число (номер билета)"))
i=6
SumOfFirstThreeDigits=SumOfThreeDigits(i)
print(SumOfThreeDigits(i))
i=3
SumOfLastThreeDigits=SumOfThreeDigits(i)
print(SumOfThreeDigits(i))
if SumOfFirstThreeDigits==SumOfLastThreeDigits:
    print ("yes")
else:
    print ("no")

