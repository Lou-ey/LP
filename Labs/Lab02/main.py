from Node import Node
from LinkedList import *

if __name__ == "__main__":
    my_node = Node(44)

    my_node_value = my_node.get_value()
    print("my_node_value: ", my_node_value)

    linked_list = LinkedList(my_node_value)

    head_node = linked_list.get_head_node()

    ll = LinkedList(5)
    ll.insert_beginning(70)
    ll.insert_beginning(5675)
    ll.insert_beginning(90)
    ll.insert_beginning(70)
    print(ll.stringify_list())

    #ll.remove_first_instance_node(70)
    #print(f'Before the swap: {ll.stringify_list()}')
    #ll.remove_all_instances_nodes(70)
    #ll.swap_nodes(90, 5)
    #print(f'After the swap: {ll.stringify_list()}')


    nth_last = nth_last_node(ll, 1)
    print(nth_last.value)

    middle_node = middle_node(ll)
    print(middle_node.value)