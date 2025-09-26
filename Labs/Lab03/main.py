from DoublyLinkedList import DoublyLinkedList

if __name__ == '__main__':
    subway = DoublyLinkedList()
    subway.add_to_head('Times Square')
    subway.add_to_head('Grand Central')
    subway.add_to_head('Central Park')
    subway.add_to_tail('Peen Station')
    subway.add_to_tail('Wall Street')
    subway.add_to_tail('Brooklyn Bridge')

    print(f'{subway.stringify_list()}')

    subway.remove_by_value('Central Park')
    subway.remove_by_value('Brooklyn Bridge')
    subway.remove_by_value('Times Square')

    print(f'After removing Central Park and Brooklyn Bridge and Times Square: {subway.stringify_list()}')