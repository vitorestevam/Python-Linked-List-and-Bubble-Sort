class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def at_start(self,dataAux):
        nodeActual= Node(dataAux)
        if(self.head is None):  #empty list
            self.head=nodeActual
        else:                   #not empty list
            nodeActual.next=self.head
            self.head=nodeActual
    
    def return_list(self):
        message= "{"
        nodeActual=self.head

        while(nodeActual != None):
            message+= str(nodeActual.data)+", " 
            nodeActual=nodeActual.next
        
        message= message[:-2]
        message+="}"
        return(message)

    def get_by_index(self, index):
        aux=self.head
        for i in range(index):
            aux=aux.next
        return aux
    
    def get_length(self):
        aux=self.head
        length=0
        while(aux is not None):
            length+=1
            aux=aux.next
        return length

    # def change_data_by_index(self,index,data):
    #     aux=self.head
    #     for i in range(index):
    #         aux=aux.next

    #     aux.data=data

    def bubble_sort(self):
        for size in range(self.get_length()-1,0,-1): #get the highest index that will reach
            nodeActual=self.head
            for i in range(size): #index to read the elements from 0 to size
                nodeNext=nodeActual.next
                if(nodeActual.data>nodeNext.data):
                    temp=nodeNext.data
                    nodeNext.data=nodeActual.data
                    nodeActual.data=temp
                    
                nodeActual=nodeActual.next

    def bubble_sort_image_by_hue(self):
        #print("tamanho:",self.get_length())
        for size in range(self.get_length()-1,0,-1): #get the highest index that will reach
            nodeActual=self.head
            for i in range(size): #index to read the elements from 0 to size
                nodeNext=nodeActual.next
                if(nodeActual.data[2]>nodeNext.data[2]): #compara a hue
                    temp=nodeNext.data
                    nodeNext.data=nodeActual.data
                    nodeActual.data=temp
                    
                nodeActual=nodeActual.next


