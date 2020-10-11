import numpy as np
import cv2 as cv
from linkedList import LinkedList 
from imageControl import ImageControl 


img = ImageControl("brilho.jpg")
img.show_image()
img.order_pixels()
img.show_custom_image()

#img.order_pixels()
#img.show_list()
#img.show_custom_image()

cv.waitKey(0)
cv.destroyAllWindows()