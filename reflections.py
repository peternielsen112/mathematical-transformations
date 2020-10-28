docalculation = True
axischeck = False
axis = input("Enter the axis of reflection (x/y): ")
pointx = int(input("Enter the x coordinate of the point: "))
pointy = int(input("Enter the y coordinate of the point: "))
if axis == str("x"):
  axischeck = True
  axis = int(0)
elif axis == str("y"):
  axischeck = True
  axis = int(1)
else:
  print("Improper axis input.")
  axischeck = False
if axischeck == False:
  docalculation = False
while axischeck == True:
  if axis == 1:
    pointxnew = (pointx * -1)
    pointynew = pointy
    break
  elif axis == 0:
    pointxnew = pointx
    pointynew = (pointy * -1)
    break
  else:
    docalculation = False
    break
  break
if docalculation == True:
  print("Reflected Point: (",pointxnew,",",pointynew,")")
