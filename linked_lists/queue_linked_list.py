from linked_lists.linked_list import DataNode, LinkedList


class QueueLinkedList(LinkedList):
    def __init__(self):
        self.__head = None
        self.__tail = None

    def add(self, new_data):
        new_element = DataNode(new_data)
        if self.__head is None:
            self.__head = new_element
        else:
            self.__tail.set_next_elem(new_element)
        self.__tail = new_element

    def pop(self):
        if self.__head is None:
            raise ValueError('Collection is empty!')

        node = self.__head
        self.__head = self.__head.get_next_elem()
        return node.data
