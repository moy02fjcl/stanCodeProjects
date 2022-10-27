"""
File: add2.py
Name: Tracy Lee
------------------------
TODO:
"""

import sys


class ListNode:
    """
    To define a linked list, each node including data and the reference of the next data.

    val: the data of the node
    next: to the reference of the next node
    """
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    l1 and l2 are linked lists that concatenate numbers from single digits.
    To restore the linked lists of l1 and l2 to numbers and add them together,
    and then concatenate them into a new linked list.

    :param l1: ListNode; the first node to linked list 1(l1)
    :param l2: ListNode; the first node to linked list 2(l2)
    :return: ListNode; the first node to a linked list
    """
    num1 = convert_to_number(l1)
    num2 = convert_to_number(l2)
    total = str(num1 + num2)
    link_list = None
    for i in range(len(total)-1, -1, -1):
        node = ListNode(int(total[i]), None)
        if link_list is None:
            link_list = node
            cur = link_list
        else:
            cur.next = node
            cur = cur.next
    return link_list


def convert_to_number(head):
    """
    This function
    :param head: ListNode;
    :return: int;
    """
    cur = head
    num = 0
    power = 0
    while cur is not None:
        num += cur.val * (10 ** power)
        power += 1
        cur = cur.next
    return num



####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
