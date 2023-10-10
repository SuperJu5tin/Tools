import math

"""
vₓ = vₓ₀ + aₓt
x = x₀ + vₓ₀t + (aₓ * t²) / 2
vₓ² = vₓ₀² + 2aₓ(x - x₀)
"""


def velocity_x():
  print("velocity_x")


def distance():
  print("distance")


def velocity_x_squared():
  print("velocity_x_squared")


def main():
  done = False

  while not done:

    print("Equation types:")
    print("\t1. vₓ = vₓ₀ + aₓt")
    print("\t2. x₀ + vₓ₀t + (aₓ * t²) / 2")
    print("\t3. vₓ² = vₓ₀² + 2aₓ(x - x₀)")
    print("\t . None")

    equation_type = input("Enter equation: ").lower()

    if equation_type == '1':
      velocity_x()
    elif equation_type == '2':
      distance()
    elif equation_type == '3':
      velocity_x_squared()
    elif equation_type == '.':
      done = True
    else:
      print("\nTry again \n")


if __name__ == '__main__':
  main()
