from imutils import paths
import cv2
import numpy as np
from PIL import Image,ImageChops

from google.colab.patches import cv2_imshow

imagePaths = list(paths.list_images('/content/photos'))

for imagePath in imagePaths:
  image = cv2.imread(imagePath)
  gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  def mse(imagePaths, gray):
    h,w = imagePaths.shape
    diff = cv2.subtract(imagePaths, gray)
    err = np.sum(diff**2)
    mse = err/(float(h*w))
    return mse
  def any_diff():
    imagepaths,gray=Image.open('imagePaths'),Image.open('gray)')
    diff=ImageChops.difference(imagePaths,gray)
    if diff.getbbox():
      diff.show()
    else:
      print("no difference")
  print(mse.__doc__)
  print(any_diff.__doc__)
  #cv2_imshow(gray)

