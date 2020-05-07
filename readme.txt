dado una lista c de leng(n)
donde c[i] E {0,1}  
c[0] && c[n-1] == 0
if c[i-1] == 1: c[i] = 0

ej = [0,1,0,0,0,1,0,1,0]

encontrar la forma optima de llegar de c[0] a c[n] avansando i+1 o i+2 sin caer en un 1