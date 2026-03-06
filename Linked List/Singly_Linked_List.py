class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        
    # INSERT AT END
    def InsertAtEnd(self,value):
        temp=Node(value)
        if (self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp
            
    # INSERT AT BEGINING
    def InsertAtBeg(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp
        
    # INSERT AT ANY POSITION
    def InsertAtAny(self,value,x): # here x = the data of node after which we want to insert the new node
        temp=Node(value)
        t1=self.head
        while(t1.next!=None):
            if(t1.data==x):
                temp.next=t1.next
                t1.next=temp
            t1=t1.next
            
    # DELETE AT ANY POSITION
    def DeleteAnElement(self,value):
        t1=self.head
        prev=t1
        if(t1.data==value):
            self.head=t1.next
        while(t1.next!=None):
            if(t1.data==value):
                prev.next=t1.next
                break
            else:
                prev=t1
                t1=t1.next
        if(t1.data==value):
            prev.next=None
                
    # PRINTING THE LINKED LIST
    def PrintLL(self):
        t1=self.head
        while(t1.next!=None):
            print(t1.data,"->",end=' ')
            t1=t1.next
        print(t1.data)
    # CREATING THE OBJECT AND CALLING THE FUNCTIONS
obj=SinglyLinkedList()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.InsertAtBeg(5)
obj.InsertAtAny(25,20)
obj.DeleteAnElement(30)
obj.PrintLL()