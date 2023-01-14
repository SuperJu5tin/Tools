import math

def standard(): 

  a = float(input("\nEnter a: "))
  b = float(input("\nEnter b: "))
  c = float(input("\nEnter c: "))

  vertexX = -b/2
  vertexY = a * vertexX ** 2 + b * vertexX + c

  print("\n\tStandard: " + str(a) + "x^2 + " + str(b) + "x + " + str(c))
  print("\tVertex: (" + str(vertexX) + ", " + str(vertexY) + ")")

  discriminant = b ** 2 - (4 * a * c)

  if discriminant > 1:

    x1 = (-b + (math.sqrt(discriminant))) / (2 * a)
    x2 = (-b - (math.sqrt(discriminant))) / (2 * a)

    print("\tFactored [" + x1 + ", " + x2 + "]")

  elif discriminant == 0:

    x = -b / (2 * a)

    print("\tFactored: [" + str(x) + "]")

  elif discriminant < 1:

    x1 = (-b + (math.sqrt(-discriminant))) / (2 * a)
    x2 = (-b - (math.sqrt(-discriminant))) / (2 * a)

    print("\tFactored: [" + str(x1) + "i, " + str(x2) + "i]")

def vertex():

  a = float(input("\nEnter a: "))
  h = float(input("\nEnter h: "))
  k = float(input("\nEnter k: "))

  b = -2 * h

  c = (h ** 2) + k

  vertexX = h
  vertexY = k

  print("\n\tStandard: " + str(a) + "x^2 + " + str(b) + "x + " + str(c))
  print("\tVertex: (" + str(vertexX) + ", " + str(vertexY) + ")")

  discriminant = b ** 2 - (4 * a * c)

  if discriminant > 1:

    x1 = (-b + (math.sqrt(discriminant))) / (2 * a)
    x2 = (-b - (math.sqrt(discriminant))) / (2 * a)

    print("\tFactored: [" + str(x1) + ", " + str(x2) + "]")

  elif discriminant == 0:

    x = -b / (2 * a)

    print("\tFactored: [" + str(x) + "]")

  elif discriminant < 1:

    x1 = (-b + (math.sqrt(-discriminant))) / (2 * a)
    x2 = (-b - (math.sqrt(-discriminant))) / (2 * a)

    print("\tFactored: [" + str(x1) + "i, " + str(x2) + "i]")

def factored():

  a = float(input("\nEnter a: "))
  r1 = float(input("\nEnter r1: "))
  r2 = float(input("\nEnter r2: "))

  b = -r1 + -r2
  c = -r1 * -r2

  vertexX = -b/2
  vertexY = a * vertexX ** 2 + b * vertexX + c

  x1, x2 = r1, r2

  print("\n\tStandard: " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + "")
  print("\tVertex: (" + str(vertexX) + ", " + str(vertexY) + ")")
  print("\tFactored: [" + str(x1) + ", " + str(x2) + "]")

def quadratic():

  while True:

    input()

    print("\nForms: \n\t1. Standard (ax^2 + bx + c) \n\t2. Vertex ( a( x - h )^2 + k) \n\t3. Factored ( a( x - r1 )( x - r2 )) \n\t . None \n")

    equationType = input("Enter equation: ").lower()
    
    if equationType == '1':
      standard()

    elif equationType == '2':
      vertex()

    elif equationType == '3':
      factored()

    elif equationType == '.':
      break
    else:
      print("\nTry again \n")


while True:
  
  input()

  print("Equation types: \n\t1. Quadratic \n\t . None \n")

  equationType = input("Enter equation: ").lower()
  
  if equationType == '1':
    quadratic()
  
  elif equationType == '.':
    break

  else:
    print("\nTry again \n")