class HashMap:
    def __init__(self, array_size=10):
        self.array_size = array_size
        self.array = [None for _ in range(array_size)] # initializes self.array of length array_size where every element is set to None.

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code
