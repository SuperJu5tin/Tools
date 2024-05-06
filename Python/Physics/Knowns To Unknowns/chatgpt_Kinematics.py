def kinematics_solver():
  print("Welcome to the Kinematics Solver!")
  print("Please enter the known variables:")

  known_variables = []

  # Ask the user for known variables
  initial_velocity = input("Initial Velocity (m/s, 0 if unknown): ")
  known_variables.append(('u', initial_velocity))

  final_velocity = input("Final Velocity (m/s, 0 if unknown): ")
  known_variables.append(('v', final_velocity))

  acceleration = input("Acceleration (m/s², 0 if unknown): ")
  known_variables.append(('a', acceleration))

  time = input("Time (s, 0 if unknown): ")
  known_variables.append(('t', time))

  displacement = input("Displacement (m, 0 if unknown): ")
  known_variables.append(('s', displacement))

  # Filter out unknown variables
  unknown_variables = [(var, value) for var, value in known_variables if float(value) == 0]

  # Ensure there are enough known variables to solve for unknowns
  if len(known_variables) - len(unknown_variables) < 3:
    print("Insufficient information to solve for unknown variables.")
    return

  # Calculate unknown variables
  for var, _ in unknown_variables:
    if var == 'u':
      u = (float(final_velocity) - float(acceleration) * float(time))
      known_variables.append(('u', u))
    elif var == 'v':
      v = (float(initial_velocity) + float(acceleration) * float(time))
      known_variables.append(('v', v))
    elif var == 'a':
      a = (float(final_velocity) - float(initial_velocity)) / float(time)
      known_variables.append(('a', a))
    elif var == 't':
      t = (float(final_velocity) - float(initial_velocity)) / float(acceleration)
      known_variables.append(('t', t))
    elif var == 's':
      s = (float(initial_velocity) * float(time) + 0.5 * float(acceleration) * float(time) ** 2)
      known_variables.append(('s', s))

  # Display the results
  print("\nResults:")
  for var, value in known_variables:
    print(f"{var} = {value} m/s" if var in ['u', 'v'] else f"{var} = {value} m")


# Run the kinematics solver
kinematics_solver()

# breaks when u input non floats, and when value = 0