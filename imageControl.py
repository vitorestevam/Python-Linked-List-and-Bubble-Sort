import numpy as np
import cv2 as cv
import time
from linkedList import LinkedList 

class ImageControl:
    
    def __init__(self,source):
        self.imgBGR = cv.imread(source,1)
        self.imgRows,self.imgCols,z = self.imgBGR.shape

        self.customImg=np.zeros((self.imgRows,self.imgCols,z),np.uint8)

        self.imgList=LinkedList()

        print(self.imgBGR.shape)

    def show_image(self):
        cv.imshow('BGR',self.imgBGR)

    def show_custom_image(self):
        self.customImg=cv.cvtColor(self.customImg, cv.COLOR_HSV2BGR)
        cv.imshow('custom',self.customImg)

    def show_list(self):
        for i in range(self.imgList.get_length()):
            print(self.imgList.get_by_index(i).data.return_list())

    def image_to_linked_list(self):
        for row in range(0,self.imgRows,1):
            list=LinkedList()
            for col in range(0,self.imgCols,1):
                pixel=self.imgBGR[row][col]
                list.at_start(pixel)                

            self.imgList.at_start(list) #add row

    def linked_list_to_image(self):
        for row in range(self.imgRows-1,0,-1):
            pxrow=self.imgList.get_by_index(row).data
            for col in range(self.imgCols-1,0,-1):
                pixel=pxrow.get_by_index(col).data
                #pixel=self.imgBGR[row][col]
                self.customImg[self.imgRows - row][self.imgCols - col] = pixel

    def order_pixels(self):
        time.sleep(1)
        self.imgBGR=cv.cvtColor(self.imgBGR, cv.COLOR_BGR2HSV)
        self.image_to_linked_list()
        for row in range(self.imgRows):
            pxrow=self.imgList.get_by_index(row).data
            # print(pxrow.getength())
            #print(str(pxrow.return_list())+'\n')
            pxrow.bubble_sort_image_by_hue()

        self.linked_list_to_image()