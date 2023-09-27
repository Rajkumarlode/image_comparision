from imutils import paths
import cv2
import numpy as np
from PIL import Image,ImageChops
import matplotlib.pylab as plt
imagepaths=list(paths.list_images('C:\Users\RAJ\Desktop\compare_images\catsimages'))
from google.colab.patches import cv2_imshow
class originalGray:
       def show_original(self):
              for i in imagepaths:
                     image=cv2.imread(i)
                     cv2_imshow(image)
                     cv2.waitKey(0)
               cv2.destroyAllWindows()
      def show_grayscale(self):
             for i in imagepaths:
                    image=cv2.imread(i)
                    gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    cv2_imshow(gray)
                    cv2.waitKey(0)
             cv2.destroyAllWindows()
       
      
             
class Comparaing(originalGray):
       def RGB_channels(self):
              # Display RGB Channels of our image
               for i in imagepaths:
               fig, axs = plt.subplots(1, 3, figsize=(15, 5))
               axs[0].imshow(image[:,:,0], cmap='Reds')
               axs[1].imshow(image[:,:,1], cmap='Greens')
               axs[2].imshow(image[:,:,2], cmap='Blues')
               axs[0].axis('off')
               axs[1].axis('off')
               axs[2].axis('off')
               axs[0].set_title('Red channel')
               axs[1].set_title('Green channel')
               axs[2].set_title('Blue channel')
               plt.show()
       def sharpen_image(self):
              for i in imagepaths:
                     kernel_sharpening = np.array([[-1,-1,-1],
                                                [-1,9,-1],
                                                [-1,-1,-1]])
                     sharpened = cv2.filter2D(i, -1, kernel_sharpening)

                     fig, ax = plt.subplots(figsize=(8, 8))
                     ax.imshow(sharpened)
                     ax.axis('off')
                     ax.set_title('Sharpened Image')
                     plt.show()
       def blure_image(self):
              #Blurring the image
              for i in imagepaths:
                     kernel_3x3 = np.ones((3, 3), np.float32) / 9
                     blurred = cv2.filter2D(i, -1, kernel_3x3)
                     fig, ax = plt.subplots(figsize=(8, 8))
                     ax.imshow(blurred)
                     ax.axis('off')
                     ax.set_title('Blurred Image')
                     plt.show()
      
class meandifference(comparing):
       def mean_difference(self):
              imagepaths=list(paths.list_images('/content/catsimages'))
              for i in imagepaths:
                     image=cv2.imread(i)
                     gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                     for j in gray:
                            gray_image = cv2.imread(j, cv2.IMREAD_GRAYSCALE)
                            # Calculate the absolute difference between the two images
                            color_difference = cv2.absdiff(i, cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR))
                            # Calculate the mean color difference
                            mean_difference = np.mean(color_difference)
                            print(f"Mean Color Difference: {mean_difference}") 
                            #cv2_imshow(gray)
                            #cv2_imshow(image)
                            cv2.waitKey(0)
                     cv2.destroyAllWindows()

#calling  the methods.

obj=originalGray()         
obj1=comparing()
obj2=meandifference()
obj.show_original()
obj.show_grayscale()
obj1.RGB_channels()
obj1.sharpen_image()
obj1.blure_image()
obj2.mean_difference()

