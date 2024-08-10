import cv2
import numpy as np
# import OS module
import os
# Get the list of all files and directories
path = "images"
dir_list = os.listdir(path)
print(dir_list)
matchlist=[]
for x in dir_list:
  fpath="images/"+x
  original = cv2.imread("a1.jpg")
  duplicate = cv2.imread(fpath)


  if original.shape == duplicate.shape:
      difference = cv2.subtract(original, duplicate)
      b, g, r = cv2.split(difference)

      if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        matchlist.append(fpath)

if len(matchlist)>0:
  print("Match images are ",matchlist)
else:
  print("No Plagarism")
