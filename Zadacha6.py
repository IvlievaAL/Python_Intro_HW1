# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
def SumOfThreeDigits (digit):
    i=0
    Sum=0
    while i<3:
        Sum=Sum+N%10**digit//10**(digit-1)
        digit-=1
        i+=1
    return Sum
N=int(input ("Введите шестизначное число (номер билета)"))
digit=6
SumOfFirstThreeDigits=SumOfThreeDigits(digit)
digit=3
SumOfLastThreeDigits=SumOfThreeDigits(digit)
if SumOfFirstThreeDigits==SumOfLastThreeDigits:
    print ("yes")
else:
    print ("no")

