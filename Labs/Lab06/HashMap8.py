class HashMap:
    def __init__(self, array_size=10):
        self.array_size = array_size
        self.array = [None for _ in range(array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):
        modulus = hash_code % self.array_size
        return modulus

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]
        if current_array_value is None:
            self.array[array_index] = [key, value]
        elif current_array_value[array_index] == key:
            self.array[array_index][1] = value
        elif current_array_value[0] != key:
            pass

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]
        if possible_return_value is not None:
            if possible_return_value[0] == key:
                return possible_return_value[1]
        return None


hash_map = HashMap(20)
hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gneiss"))
