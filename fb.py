import math as mt
print("SECUENCIA DE FIBONACCI")


n1=1
n2=1
print(n1)
print(n2)
n3=n1+n2
print(n3)

while n3<1000:
	n1=n2 #asignando valores
	n2=n3
	n3=n1+n2
	if n3>1000:
		print("El codigo imprime la secuencia hasta 1000")
		break
	print(n3)
				
		
	
		

