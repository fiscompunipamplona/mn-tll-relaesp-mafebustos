import math as mt

print("Cambio de coordenadas polares a coordenadas cartesianas.")

r=float(input("Digitar un valor para r= "))
a=float(input("Digitar un valor para el angulo a= "))
t=((a*mt.pi)/180)
x=r*mt.cos(t)
y=((r)*(mt.sin(t)))
print("El valor de x=",x)
print("El valor de y=",y)


