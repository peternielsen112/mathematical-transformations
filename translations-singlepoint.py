originx = float(input("Enter the current x value of the point: "))
originy = float(input("Enter the current y value of the point: "))

change1 = input("Choose the change type for x (left/right): ")
numericalx = float(input("Enter the x change number (positive number): "))
change2 = input("Choose the change type for y (up/down): ")
numericaly = float(input("Enter the y change number (positive number): "))


xneg = False
yneg = False
invalid = False

while True:
  if change1 == "left":
    xneg = True
  elif change1 == 'right':
    xneg = False
  else:
    print("Invalid input for x change type.")
    break
    invalid = False
  if change2 == 'down':
    yneg = True
  elif change2 == 'up':
    yneg = False
  else:
    print("Invalid input for y change type.")
    invalid = True
    break
  if xneg == True:
    numericalx = (numericalx * -1)
  else:
    pass
  if yneg == True:
    numericaly = (numericaly * -1)
  else:
    pass
  global newx
  newx = (numericalx + originx)
  global newy
  newy = (numericaly + originy)
  break
if invalid == True:
  print("Unfortunately, the program could not complete it's calculations due to an input error.")
elif invalid == False:
  print("New point value: (",newx," , ",newy,")")
