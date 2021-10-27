from typing import Sequence


class LinkedList:

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
    
    def __init__(self):
        self.head = self.Node(0)    # virtual head
        self.size = 0               # total nodes excluding virtual head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if 0 <= index and index < self.size:
            node = self.head
            for _ in range(index+1):
                node = node.next
            
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        # new_node = self.Node(val)
        # if self.head.next != None:
        #     new_node.next = self.head.next
        
        # self.head.next = new_node
        # self.size += 1
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # node = self.head
        # for _ in range(self.size):
        #     node = node.next
        # node.next = self.Node(val)
        # self.size += 1
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            index = 0
        elif index > self.size:
            return
        
        new_node = self.Node(val)
        prev, cur = None, self.head
        for _ in range(index+1):
            prev, cur = cur, cur.next

        prev.next = new_node
        new_node.next = cur
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index and index < self.size:
            prev, cur = None, self.head
            for _ in range(index+1):
                prev, cur = cur, cur.next
            prev.next = cur.next
            self.size -= 1
        else:
            return


if __name__ == '__main__':
    myLinkedList = LinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)
    print(myLinkedList.get(1))
    myLinkedList.deleteAtIndex(1)
    print(myLinkedList.get(1))


    # node = myLinkedList.head
    # while node != None:
    #     print(node.val)
    #     node = node.next