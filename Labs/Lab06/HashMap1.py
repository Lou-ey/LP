class HashMap:
    def __init__(self, array_size=10):
        self.array_size = array_size
        self.array = [None for _ in range(array_size)]
