import ctypes
# imports libraries which can perform c operations
import sys
# used to check the size of objects
class MeraList():

    def __init__(self):
        self.size=1
        self.n=0

        # fuction to create a array of size self.size
        self.A= self.__make_array__(self.size)

    def __make_array__(self,capacity):
        # creates the array of size capacity
        return (capacity*ctypes.py_object)()
    
    # magic function to return the length of list
    def __len__(self):
        return self.n
    
    def __append(self,new_item):
        #check if list has empty space 
        if self.size==self.n:
            #resize
            self.__resize(self.size+8)
        
        # appending the new_item
        self.A[self.n]=new_item
        self.n+=1
    
    def __resize(self,new_capacity):
        # call the make arraay function
        B = self.__make_array__(new_capacity)
        self.size=new_capacity

        #copy the content of the list into the new list 
        for i in range(self.n):
            B[i]==self.A[i]
        # Reassign the List b as list A
        self.A = B



    
L=MeraList()
# print(sys.getsizeof(L))
print(len(L))
