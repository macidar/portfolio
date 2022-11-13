# poda określoną ilość liczb pierwszych.prime numbers
# potrzebny będzie moduł math i metoda math.sqrt(x)
# zamiast funkcji range będzie użyta pętla bo będzie dużo obliczeń a pętla jest szybsza
deal_num=int(input("Podaj ile chcesz liczb pierwszych: "))
print()
import math
number_loops=1
number=1
prime_numbers=[]
divisor=2
while number_loops<deal_num:
    number=number+2
    divisor=2
    while number%divisor!=0 and divisor<math.sqrt(number):
                    divisor=divisor+1
    if number%divisor!=0 :prime_numbers.append(number)       
    number_loops=len(prime_numbers)
print ("ZBIÓR PIERWSZYCH",deal_num,"LICZB PIERWSZYCH: ")
print()
print(prime_numbers)
print()
print("NAJWYZSZA CZYLI",deal_num,"TO: ",prime_numbers[-1])