import math

"""
vₓ = vₓ₀ + aₓt
x = x₀ + vₓ₀t + (aₓ * t²) / 2
vₓ² = vₓ₀² + 2aₓ(x - x₀)
"""


def main():
  done = False

  while not done:

    print("Enter Knowns:")
    print("\t . None")

    v_x = "test"
    v_x_initial = "test2"
    x = "test3"
    a = "test4"
    t = "test5"

    placeholder = input("Enter equation: ").lower()

    # Possible class/object and for each to figure out which ones exist and which don't, {variable: { known: Boolean, value: int }, variable2: { known: Boolean, value: int }, etc}
    # detect blank "" for unknown

    # if equation_type == '1':
    #   velocity_x()
    # elif equation_type == '2':
    #   distance()
    # elif equation_type == '3':
    #   velocity_x_squared()
    # elif equation_type == '.':
    #   done = True
    # else:
    #   print("\nTry again \n")


if __name__ == '__main__':
  main()
