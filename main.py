import numpy as np
import cv2 as cv
from linkedList import LinkedList 
from imageControl import ImageControl 


img = ImageControl("image.jpg")
img.show_image()
img.image_to_linked_list()
#img.show_list()
img.linked_list_to_image()

img.show_custom_image()

cv.waitKey(0)
cv.destroyAllWindows()