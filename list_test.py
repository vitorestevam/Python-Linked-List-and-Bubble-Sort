from linkedList import LinkedList 

list = LinkedList()
list.at_start(3)
list.at_start(1)
list.at_start(2)
list.at_start(5)
print(list.return_list())
list.bubble_sort()
print(list.return_list())
