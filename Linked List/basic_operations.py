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
    def find_middle_brute(self):
        temp=self.head
        count=0
        while(temp.next!=None):
            count=count+1
            temp=temp.next
        count+=1
        temp=self.head
        for i in range(0,count//2):
            temp=temp.next
        print("middle node of linked list is (brute) :",temp.data)
    def find_middle_optimal(self): # slow and fast pointer approach
        slow=self.head
        fast=self.head
        while(fast is not None and fast.next is not None):
            slow=slow.next
            fast=fast.next.next
        print("The middle node of linked list is (optimal):",slow.data)
obj=SinglyLinkedList()
obj.InsertAtAnyPosition(10,0)
obj.InsertAtAnyPosition(20,1)
obj.InsertAtAnyPosition(30,2)
obj.InsertAtAnyPosition(40,3)
obj.InsertAtAnyPosition(50,4)
obj.InsertAtAnyPosition(60,5)
obj.PrintLL()
obj.CountLengthOfLL()
obj.find_middle_brute()
obj.find_middle_optimal()
        
            
    