from Node import Node

if __name__ == "__main__":

    yacko = Node("likes to yak")
    wacko = Node("has a penchant for hoarding snacks")
    dot = Node("enjoys spending time in movie lots")

    yacko.link_node = dot # Link yacko to dot
    dot.link_node = wacko # Link dot to wacko

    dots_data = yacko.link_node.data
    wackos_data = dot.link_node.data

    dot_from_yacko = yacko.link_node # Get dot node from yacko
    wacko_from_yacko = dot_from_yacko.link_node.data # Get wacko node from dot

    print(f"Dot: {dots_data}")
    print(f"Wacko: {wackos_data}")
    print(f"Yacko: {yacko.data}")

    #
