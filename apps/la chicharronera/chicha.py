from math import sqrt

a = float(input("Ingresa valor de a:"))
b = float(input("Ingresa valor de b:"))
c = float(input("Ingresa valor de c:"))
try:
    if a != 0:
        x1 = (-b+sqrt((b**2)-(4*a*c)))/(2*a)
        x2 = (-b-sqrt((b**2)-(4*a*c)))/(2*a)
        if x1 == 0 and x2 == 0:
            print("Solucion: x=%4.3f" % x1)
        else:
            print("Soluciones: x1=%4.3f y x2=%4.3f"%(x1,x2))
except:
    print("Hubo algrun problema")