#dzielniki
number=int(input("Podaj liczbę której dzielnik chcesz znaleźć "))
potential=[]
divisors=[]
i=2
while i<number:
    potential.append(i)
    i=i+1
for divisor in potential:
    if number%divisor==0:
        divisors.append(divisor)
print("Liczba ",number," jest pododzielna przez: ", divisors)
max=divisors[-1]
print("Najwyższy dzielnik ",number, " to: ",max)
