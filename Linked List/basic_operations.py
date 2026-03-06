class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def InsertAtAnyPosition(self,value,position):
        newnode=Node(value)
        if(position==0):
            newnode.next=self.head
            self.head=newnode
        else:
            current=self.head
            prev_node=current
            count=0
            while(current is not None and count<position):
                prev_node=current
                current=current.next
                count+=1
                # linking previous to new,and new to current
            prev_node.next=newnode
            newnode.next=current
    def CountLengthOfLL(self):
        count=0
        current=self.head
        while(current.next!=None):
            count+=1
            current=current.next
        print("Length of Linked List is :",count+1)
    def PrintLL(self):
        current=self.head
        while(current is not None):
            print(current.data,"->",end=' ')
            current=current.next
        print("None")
obj=SinglyLinkedList()
obj.InsertAtAnyPosition(10,0)
obj.InsertAtAnyPosition(20,1)
obj.InsertAtAnyPosition(30,2)
obj.InsertAtAnyPosition(40,3)
obj.PrintLL()
obj.CountLengthOfLL()

        
            
    