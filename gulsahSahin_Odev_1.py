import math

a = 3
b = 5
carpim = a*b
toplam = a+b
aKare = math.pow(a,2)
bKare = math.pow(b,2)

sayi = (1+a) / (1+(1/math.pow(a,2)))

y1 = math.pow(sayi,1/3) + (1 / (a*math.sqrt(a)))


sayi2 = (1 + ( (math.pow((a+(bKare)),1/3)) / (1/math.sqrt(carpim)) ))

y2 = ((a+(a/(b+1))) / math.pow(sayi2,1/5) ) + (math.pow((carpim),2)) - ( 4 * (a/math.pow((bKare),1/3)) )


sayi3 = ( (a+b) / (math.pow((aKare+bKare),4)) ) / (( carpim / (1+(1/(a+(1/b+math.pow((carpim*b),1/5))))) ))

y3 = ( math.pow(sayi3,1/3) ) + ( (math.pow(a,2) + math.pow(b,3)) / ( (carpim / (math.pow(toplam,2))) + (3*(a-b)*toplam)) )
- ( (math.pow(math.pow(a,3),1/4)) / (2/(math.pow(bKare,1/3))) )


print(y1)
print(y2)
print(y3)