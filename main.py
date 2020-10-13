import cv2 as cv
from imageControl import ImageControl 

#o order_pixels rderna os pixels de cada linha horizontal da imagem
#pelo seu BRILHO, indo do mais claro para o mais escuro.
#Separei 4 imagens que exemplificam 
#bem o que o script faz, mas fique a vontade para testar com a imagem que quiser.

#para fazer implementei listas encadeadas e bubblesort.
#utilizeitambém as bibliotecas open cv e numpy

#usa em uma imagem de cada vez. Deixei comentado para facilitar

img = ImageControl("images/image3.jpg")
#img = ImageControl("images/image.jpg")
# img = ImageControl("images/image2.jpg")
# img = ImageControl("images/image4.jpg")

img.show_image()
img.order_pixels()

cv.waitKey(0)
cv.destroyAllWindows()