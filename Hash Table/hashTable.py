class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0

        for letter in key:
            # Any prime number can be here instead of 23
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash

    def set_items(self, key, val):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, val])

    def get_item(self, key):
        index = self.__hash(key)

        if self.data_map[index] is not None:

            # for element in self.data_map[index]:
            #     if element[0] == key:
            #         return element[1]
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]

        return None

    def get_keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])

        return all_keys

    def printTable(self):
        for i, val in enumerate(self.data_map):
            print(f"{i}: {val}")
