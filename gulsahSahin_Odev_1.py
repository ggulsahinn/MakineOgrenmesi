import math

a = 3
b = 5

sayi = math.pow(((1+a) / (1+(1/math.pow(a,2)))), 1/3)

y1 = sayi + (1/(a*(math.sqrt(a))))

print(y1)

sayi2 = math.pow((1+(math.pow((a+math.pow(b,2)),1/3))/(1/math.sqrt(a*b))), 1/5)

y2 = (a+(a/(b+1))) / sayi2  + math.pow((a*b),2) - (4 * (a/math.pow((math.pow(b,2)),1/3)))

print(y2)