import math as mt

print("La nave espacial viaja desde la tierra a una velocidad que corresponde a una fracción de c (velocidad de la luz)[m/s]")
n=float(input("Digite la velocidad como fraccion de c= "))
c=3e8 #m/s
v=(c*n)#m/s
a=float(input("Digite la distancia años luz [ly] a la que se encuentra el otro planeta: ")) #ly
x= ((a*9.46e15)) #m
t=(x/v) #seg

print("el tiempo que tardó la nave espacial en ir hasta el planeta visto desde la tierra es t= ",t,"[s]") #seg

l=(mt.sqrt(1-((v**2)/(c**2))))

tp=((t-((v*x)/(c**2)))/l)
print("El tiempo que tardó la nave en ir hasta el otro planeta visto desde la nave espacial es tp= ",tp,"[s]")

