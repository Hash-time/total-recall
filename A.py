import math
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# Ввод, если два числа и более в одну строку
(a, b,c,) = [int(s) for s in input().split()]
(h, l) = [int(s) for s in input().split()]
n=(a*b+b*c+a*c)*2-a*b
n=n-0.15*n
m=h*0.001
p=l*0.001
j=m*p
j=j-0.1*j
u=n/j
print(math.ceil(u))