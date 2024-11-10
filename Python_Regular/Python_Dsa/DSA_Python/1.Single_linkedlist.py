
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

#1.check each element
def traverse(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next
    print()
#2.target check
def find_element(head, target=3):
    current = head
    while current is not None:
        if current.data == target:
            return True
        current = current.next
    return False

#3.length of list
def lengthlist(head):
    length = 0
    current = head
    while current is not None:
        length += 1
        current=current.next
    print(f"the length of linkedlist:{length}")

#4.Insert element in first
def insert_first(head,value):
    new_node = Node(value)
    new_node.next = head
    head = new_node

def main():
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(6)

    print("Linked List:", end=" ")
    printList(head)
    traverse(head)
    find_element(head,target=3)
    lengthlist(head)
    insert_first(head,1)

if __name__ == "__main__":
    main()
