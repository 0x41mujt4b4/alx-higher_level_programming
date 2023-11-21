#!/usr/bin/python3
""" Define Singly Linked List"""


class Node:
    """A class that represent a Node"""
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """A class that represent a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        new_node.next_node = self.__head
        self.__head = new_node

    def __str__(self):
        tmp = self.__head
        print_node = []
        while tmp:
            print_node.sort()
            print_node.append(str(tmp.data))
            tmp = tmp.next_node
        print_node.sort(key=int)
        return ("\n".join(print_node))
