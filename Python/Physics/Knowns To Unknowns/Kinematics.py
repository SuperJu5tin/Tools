import math

"""
vₓ = vₓ₀ + aₓt
x = x₀ + vₓ₀t + (aₓ * t²) / 2
vₓ² = vₓ₀² + 2aₓ(x - x₀)
"""

# class unkownGetter:
#   def __int__(self, v_x, v_x_initial, x, a, t):
#     self.v_x = v_x
#     self.v_x_initial = v_x_initial
#     self.x = x
#     self.a = a
#     self.t = t
#
#   known = []
#
#   def

knowns = []
unknowns = []


def info_getter(name_of_var):
  user_input = input("\tEnter " + name_of_var + ":")

  try:
    float(user_input)
    knowns.append((name_of_var, user_input))
    return user_input
  except ValueError:
    if user_input == "":
      unknowns.append(name_of_var)
    else:
      print("Try again")
      info_getter(name_of_var)


def main():
  done = False

  while not done:
    print("\nEnter Knowns:\n")

    knowns.clear()
    unknowns.clear()

    v_x = info_getter("v_x")
    v_x_initial = info_getter("v_x_initial")
    x = info_getter("x")
    a = info_getter("a")
    t = info_getter("t")

    # print(v_x, v_x_initial, x, a, t, '\n', knowns, unknowns)

    if len(knowns) >= 3:
      print("this is solvable")
    else:
      print("Try again, you need at least 3 variables to solve")

    # Possible class/object and for each to figure out which ones exist and which don't, {variable: { known: Boolean, value: int }, variable2: { known: Boolean, value: int }, etc}

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
