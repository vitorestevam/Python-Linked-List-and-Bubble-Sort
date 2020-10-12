import cv2 as cv
from imageControl import ImageControl 

#usa em uma imagem de cada vez, deixei juntas pra facilitar

img = ImageControl("images/image.jpg")
#img = ImageControl("images/image2.jpg")
#img = ImageControl("images/image3.jpg")
#img = ImageControl("images/image4.jpg")

img.show_image()
img.order_pixels()

cv.waitKey(0)
cv.destroyAllWindows()