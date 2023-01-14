import math

def standard(): 

  a, b, c = input("\nEnter a, b, c: ").split()

  a = float(a); b= float(b); c = float(c)

  vertexX = -b/2
  vertexY = a * vertexX ** 2 + b * vertexX + c

  print(f"\n\tStandard: {a}x^2 + {b}x + {c}")
  print(f"\tVertex: ({vertexX}, {vertexY})")

  discriminant = b ** 2 - (4 * a * c)

  if discriminant > 1:

    x1 = (-b + (math.sqrt(discriminant))) / (2 * a)
    x2 = (-b - (math.sqrt(discriminant))) / (2 * a)

    print(f"\tFactored [{x1}, {x2}]\n")

  elif discriminant == 0:

    x = -b / (2 * a)

    print(f"\tFactored: [{x}]\n")

  elif discriminant < 1:

    x1 = (-b + (math.sqrt(-discriminant))) / (2 * a)
    x2 = (-b - (math.sqrt(-discriminant))) / (2 * a)

    print(f"\tFactored: [{x1}i, {x2}i]\n")

def vertex():

  a, h, k = input("\nEnter a, h, k: ").split()

  a = float(a); h= float(h); k = float(k)

  b = -2 * h

  c = (h ** 2) + k

  vertexX = h
  vertexY = k

  print(f"\n\tStandard: {a}x^2 + {b}x + {c}")
  print(f"\tVertex: ({vertexX}, {vertexY})")

  discriminant = b ** 2 - (4 * a * c)

  if discriminant > 1:

    x1 = (-b + (math.sqrt(discriminant))) / (2 * a)
    x2 = (-b - (math.sqrt(discriminant))) / (2 * a)

    print(f"\tFactored: [{x1}, {x2}]\n")

  elif discriminant == 0:

    x = -b / (2 * a)

    print(f"\tFactored: [{x}]\n")

  elif discriminant < 1:

    x1 = (-b + (math.sqrt(-discriminant))) / (2 * a)
    x2 = (-b - (math.sqrt(-discriminant))) / (2 * a)

    print(f"\tFactored: [{x1}i, {x2}i]\n")

def factored():
  a, r1, r2 = input("\nEnter a, r1 r2: ").split()

  a, r1, r2 = float(a), float(r1), float(r2)
  b = -r1 + -r2
  c = -r1 * -r2

  vertexX = -b/2
  vertexY = a * vertexX ** 2 + b * vertexX + c

  x1, x2 = r1, r2

  print(f"\n\tStandard: {a}x^2 + {b}x + {c}")
  print(f"\tVertex: ({vertexX}, {vertexY})")
  print(f"\tFactored: [{x1}, {x2}]")

def quadratic():

  while True:
    
    print("\nForms: \n\t1. Standard (ax^2 + bx + c) \n\t2. Vertex ( a( x - h )^2 + k) \n\t3. Factored ( a( x - r1 )( x - r2 )) \n")

    equationType = input("Enter equation: ").lower()
    
    if equationType == '1':
      standard()
      break

    elif equationType == '2':
      vertex()
      break

    elif equationType == '3':
      factored()
      break

    else:
      print("\nTry again \n")


while True:
  
  print("Equation types: \n\t1. Quadratic \n\t. Stop \n")

  equationType = input("Enter equation: ").lower()
  
  if equationType == '1':
    quadratic()
  
  elif equationType == '.':
    break

  else:
    print("\nTry again \n")