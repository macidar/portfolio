# najwyższy wspólny dzielnik
number1=int(input("Podaj pierwszą liczbę której dzielniki chcesz znaleźć "))
number2=int(input("Podaj drugą liczbę której dzielniki chcesz znaleźć "))
potential=[]
dyvisor1=[]
dyvisor2=[]
i=2
j=2
potential2=[]
mutual=[]
potential=[]
while i<number1:
    potential.append(i)
    i=i+1
for dziel in potential:
    if number1%dziel==0:
        dyvisor1.append(dziel)
while j<number2:
    potential2.append(j)
    j=j+1
for dziel1 in potential2:
    if number2%dziel1==0:
        dyvisor2.append(dziel1)
for el in dyvisor1:
    if el in dyvisor2:
        mutual.append(el)
if number1<number2 and number2%number1==0:
    mutual.append(number1)
elif number2<number1 and number1%number2==0:
    mutual.append(number2)
print ("Wspólne dzielniki twoich liczb to: ")
print(mutual)

print("Najwyższym wspólnym dzielnikeiem jest: ")
print(mutual[-1])


