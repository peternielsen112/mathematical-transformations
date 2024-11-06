import matplotlib.pyplot as plt

k = float(input("Enter the scale factor of the dilation: "))
dilation = 0
docalculation = True
coordnum = 3

if coordnum == 3:
  global coord1x
  coord1x = float(input("Enter the x value of the first coordinate: "))
  global coord1y
  coord1y = float(input("Enter the y value of the first coordinate: "))
  global coord2x
  coord2x = float(input("Enter the x value of the second coordinate: "))
  global coord2y
  coord2y = float(input("Enter the y value of the second coordinate: "))
  global coord3x
  coord3x = float(input("Enter the x value of the third coordinate: "))
  global coord3y
  coord3y = float(input("Enter the y value of the third coordinate: "))



if k > 0 and k < 1:
  dilation = 0
elif k > 1:
  dilation = 1
else:
  docalculation = False
  print("You entered an invalid scale factor.")
  quit()

points = [(coord1x, coord1y),(coord2x,coord2y),(coord3x,coord3y)]
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

if docalculation == True:
  coord1xnew = (coord1x * k)
  coord2xnew = (coord2x * k)
  coord3xnew = (coord3x * k)
  coord1ynew = (coord1y * k)
  coord2ynew = (coord2y * k)
  coord3ynew = (coord3y * k)
  if dilation == 0:
    print("Dilation is a reduction.")
  elif dilation == 1:
    print("Dilation is an enlargement.")
  print("Coordinates:")
  print("Point 1: (",coord1xnew,",",coord1ynew,")")
  print("Point 2: (",coord2xnew,",",coord2ynew,")")
  print("Point 3: (",coord3xnew,",",coord3ynew,")")

plotyes = input('Plot answer? (y/n) ')

if plotyes == 'y':
  points = [[coord1xnew, coord1ynew],[coord2xnew,coord2ynew],[coord3xnew,coord3ynew]]
  x_coords = [p[0] for p in points]
  y_coords = [p[1] for p in points]
  print(x_coords)
  print(y_coords)
# Plot the triangle
  plt.plot(x_coords, y_coords, 'r-')  # 'r-' specifies red lines

# Fill the triangle (optional)
  plt.fill(x_coords, y_coords, 'b', alpha=0.3)  # 'b' for blue, alpha for transparency

# Show the plot
  plt.show()
else:
    pass