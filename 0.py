from pystyle import *
import cmath
a = f"""+———+————————————————————————+ㅤ                                                                               ㅤ       
|   |        Equation        |                                        
+———+————————————————————————+  
| 1 | ax+b=0                 |
| 2 | ax²+bx+c=0             |
| 3 | ax³+bx²+cx+d=0         |
| 4 | ax⁴+bx³+cx²+dx+e=0     |
| 5 | ax⁵+bx⁴+cx³+dx²+ex+f=0 |
+———+———————————————————————―+"""
print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(a)))
x = int(Write.Input("\n\n Choose equation: ", Colors.green_to_white,interval=0.00001))
if x>4:
  import os 
  os.system("cls")
  os.system("python 0.py")
if x<1:
  import os 
  os.system("cls")
  os.system("python 0.py")
if x==1:
  print(' ax+b=0') 
  a = int(input(' a = '))
  b = int(input(' b = ')) 
  if a==b==0:
      print(' equation with countless solutions')
      import os
      os.system("python 0.py")
  if a!=0:
      print(' x =' ,-b/a)
      import os
      os.system("python 0.py")
  if a==0:
    if b!=0:
      print(' the equation has no solution')
      import os
      os.system("python 0.py")
if x==2:
  print(' ax²+bx+c=0')
  a = int(input(' a = '))
  b = int(input(' b = '))
  c = int(input(' c = '))
  if a==0:
    if b!=0:
      print(' x = ',-c/b ) 
      import os
      os.system("python 0.py")
  if a==b==c==0:
      print(' equation with countless solutions')
      import os
      os.system("python 0.py")
  if a==b==0:
    if c!=0:
      print(' the equation has no solution')
      import os
      os.system("python 0.py")
  if a!=0:
      print(' x1 =',(-b+cmath.sqrt(b**2-4*a*c))/(2*a))
      print(' x2 =',(-b-cmath.sqrt(b**2-4*a*c))/(2*a))
      import os
      os.system("python 0.py")
if x==3:
  print(' ax³+bx²+cx+d=0')
  a = int(input(' a = '))
  b = int(input(' b = ')) 
  c = int(input(' c = '))
  d = int(input(' d = '))
  if a!=0:
      print(' x1 =',(((-b**3)/(27*a**3)+(b*c)/(6*a**2)-d/(2*a))+(((b**3)/(27*a**3)-(b*c)/(6*a**2)+d/(2*a))**2+(c/(3*a)-(b**2)/(9*a**2))**3)**0.5)**(1/3)+(((-b**3)/(27*a**3)+(b*c)/(6*a**2)-d/(2*a))-(((b**3)/(27*a**3)-(b*c)/(6*a**2)+d/(2*a))**2+(c/(3*a)-(b**2)/(9*a**2))**3)**0.5)**(1/3)-b/(3*a))
      print(' x2 =',(-1/2+cmath.sqrt(-3)/2)*(((-b**3)/(27*a**3)+(b*c)/(6*a**2)-d/(2*a))+cmath.sqrt(((b**3)/(27*a**3)-(b*c)/(6*a**2)+d/(2*a))**2+(c/(3*a)-(b**2)/(9*a**2))**3))**(1/3)+(-1/2-cmath.sqrt(-3)/2)*((-b**3)/(27*a**3)+(b*c)/(6*a**2)-d/(2*a)-cmath.sqrt(((b**3)/(27*a**3)-(b*c)/(6*a**2)+d/(2*a))**2+(c/(3*a)-(b**2)/(9*a**2))**3))**(1/3)-b/(3*a))
      print(' x3 =',(-1/2-cmath.sqrt(-3)/2)*(((-b**3)/(27*a**3)+(b*c)/(6*a**2)-d/(2*a))+cmath.sqrt(((b**3)/(27*a**3)-(b*c)/(6*a**2)+d/(2*a))**2+(c/(3*a)-(b**2)/(9*a**2))**3))**(1/3)+(-1/2+cmath.sqrt(-3)/2)*((-b**3)/(27*a**3)+(b*c)/(6*a**2)-d/(2*a)-cmath.sqrt(((b**3)/(27*a**3)-(b*c)/(6*a**2)+d/(2*a))**2+(c/(3*a)-(b**2)/(9*a**2))**3))**(1/3)-b/(3*a))
      import os
      os.system("python 0.py")
  if a==0:
    if b!=0:
      print(' x1 =',(-c+(c**2-4*b*d)**0.5)/(2*b))
      print(' x2 =',(-c-(c**2-4*b*d)**0.5)/(2*b))
      import os
      os.system("python 0.py")
  if a==b==0:
    if c!=0:
      print(' x =', -d/c)
      import os
      os.system("python 0.py")
  if a==b==c==d==0:
      print(' equation with countless solutions')
      import os
      os.system("python 0.py")
  if a==b==c==0:
    if d!=0:
      print(' the equation has no solution')
      import os
      os.system("python 0.py")
if x==4:
  print(' ax⁴+bx³+cx²+dx+e=0')
  a = int(input(' a = '))
  b = int(input(' b = ')) 
  c = int(input(' c = '))
  d = int(input(' d = '))
  e = int(input(' e = '))
  if a!=0:
      print(' x1 =',-b/(4*a)-((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5)-(1/2)*(-4*((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5)**2-2*((8*a*c-3*b**2)/(8*a**2))+((b**3-4*a*b*c+8*d*a**2)/(8*a**3))/((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5))**0.5)
      print(' x2 =',-b/(4*a)-((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5)+(1/2)*(-4*((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5)**2-2*((8*a*c-3*b**2)/(8*a**2))+((b**3-4*a*b*c+8*d*a**2)/(8*a**3))/((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5))**0.5)
      print(' x3 =',-b/(4*a)+((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5)-(1/2)*(-4*((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5)**2-2*((8*a*c-3*b**2)/(8*a**2))-((b**3-4*a*b*c+8*d*a**2)/(8*a**3))/((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5))**0.5)
      print(' x4 =',-b/(4*a)+((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5)+(1/2)*(-4*((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5)**2-2*((8*a*c-3*b**2)/(8*a**2))-((b**3-4*a*b*c+8*d*a**2)/(8*a**3))/((1/2)*((-2*((8*a*c-3*b**2)/(8*a**2)))/3 +(((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3))+(c**2-3*b*d+12*a*e)/((((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)+((2*c**3-9*b*c*d+27*b**2*e+27*a*d**2-72*a*c*e)**2-4*(c**2-3*b*d+12*a*e)**3)**0.5)/2)**(1/3)))/(3*a))**0.5))**0.5)
      import os
      os.system("python 0.py")
  if a==0:
    if b!=0:
      print(' x1 =',(((-c**3)/(27*b**3)+c*d/(6*b**2)-e/(2*b))+(((c**3)/(27*b**3)-c*d/(6*b**2)+e/(2*b))**2+(d/(3*b)-(c**2)/(9*b**2))**3)**0.5)**(1/3)+((-c**3)/(27*b**3)+c*d/(6*b**2)-e/(2*b)-(((c**3)/(27*b**3)-c*d/(6*b**2)+e/(2*b))**2+(d/(3*b)-(c**2)/(9*b**2))**3)**0.5)**(1/3)-c/(3*b))
      print(' x2 =',(-1/2+((-3)**0.5)/2)*((-c**3)/(27*b**3)+c*d/(6*b**2)-e/(2*b)+(((c**3)/(27*b**3)-c*d/(6*b**2)+e/(2*b))**2+(d/(3*b)-(c**2)/(9*b**2))**3)**0.5)**(1/3)+(-1/2-((-3)**0.5)/2)*((-c**3)/(27*b**3)+c*d/(6*b**2)-e/(2*b)-(((c**3)/(27*b**3)-c*d/(6*b**2)+e/(2*b))**2+(d/(3*b)-(c**2)/(9*b**2))**3)**0.5)**(1/3)-c/(3*b))
      print(' x3 =',(-1/2-((-3)**0.5)/2)*((-c**3)/(27*b**3)+c*d/(6*b**2)-e/(2*b)+(((c**3)/(27*b**3)-c*d/(6*b**2)+e/(2*b))**2+(d/(3*b)-(c**2)/(9*b**2))**3)**0.5)**(1/3)+(-1/2+((-3)**0.5)/2)*((-c**3)/(27*b**3)+c*d/(6*b**2)-e/(2*b)-(((c**3)/(27*b**3)-c*d/(6*b**2)+e/(2*b))**2+(d/(3*b)-(c**2)/(9*b**2))**3)**0.5)**(1/3)-c/(3*b))
      import os
      os.system("python 0.py")
  if a==b==0:
    if c!=0:
      print(' x1 =',(-d+(d**2-4*c*e)**0.5)/(2*c))
      print(' x2 =',(-d-(d**2-4*c*e)**0.5)/(2*c))
      import os
      os.system("python 0.py")
  if a==b==c==0:
    if d!=0:
      print(' x =',-e/d)
      import os
      os.system("python 0.py")
  if a==b==c==d==e==0:
      print(' equation with countless solutions')
      import os
      os.system("python 0.py")
  if a==b==c==d==0:
    if e!=0:
      print(' the equation has no solution')
      import os
      os.system("python 0.py")
