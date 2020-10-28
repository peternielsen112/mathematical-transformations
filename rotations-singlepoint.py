docalculation  = True
print("Rotate a point clockwise: follow the directions for the calculation to run.")
rotatedegrees = int(input("Enter degree value of rotation (90, 180, 270): "))
pointx = int(input("Enter the x value of the point: "))
pointy = int(input("Enter the y value of the point: "))
if rotatedegrees == 90:
  pointynew = (pointy * -1)
  pointxnew = pointx
elif rotatedegrees == 180:
  pointynew = (pointy * -1)
  pointxnew = (pointx * -1)
elif rotatedegrees == 270:
  pointynew = (pointx * -1)
  pointxnew = pointy
else:
  docalculation = False
while docalculation == True:
  print("Your ",rotatedegrees," degree rotation of point (",pointx,",",pointy,"):")
  print("(",pointxnew,",",pointynew,")")
  break
if docalculation == False:
  print("There is an error in user input or in the program.")
