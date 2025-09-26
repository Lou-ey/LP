class Node:
    def __init__(self, data, link_node=None):
        self.data = data
        self.link_node = link_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def link_node(self):
        return self._link_node

    @link_node.setter
    def link_node(self, link_node):
        self._link_node = link_node