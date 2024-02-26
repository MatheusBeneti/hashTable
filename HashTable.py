class HashTable:
    def __init__(self):
        self.__table = [None] * 853
        self.__numberOfCollisions = 0

    def insertWithDivision(self, key, value):
        hashedKey = self.__hash(key)
        positionToAllocate = self.__getPositionToAllocate(hashedKey)
        self.__allocate(positionToAllocate, key, value)

    def insertWithExtration(self, key, value):
        hashedKey = self.__hash(key)
        positionToAllocate = self.__getPositionToAllocate(hashedKey)
        self.__allocate(positionToAllocate, key, value)

    def __hash(self, string):
        hash_value = 0
        for char in string:
            hash_value += ord(char)
        return hash_value

    def __getPositionToAllocate(self, hashedKey):
        return hashedKey % len(self.__table)

    def __allocate(self, position, key, value):
        if self.__table[position] is None:
            self.__table[position] = []
        else:
            self.__numberOfCollisions += 1
        self.__table[position].append((key, value))

    def getValues(self, key):
        hashedKey = self.__hash(key)
        position = self.__getPositionToAllocate(hashedKey)
        entries = self.__table[position]
        if entries is not None:
            for entry in entries:
                if entry[0] == key:
                    return entry[1]
        return None

    def exportToFile(self, filename):
        with open(filename, 'w') as file:
            for entry in self.__table:
                if entry is not None:
                    line_values = ', '.join([f"{key}:{value}" for key, value in entry])
                    file.write(line_values + '\n')

    def reset(self):
        self.__table = [None] * 853
        self.__numberOfCollisions = 0

    def digit_extraction_hash(key, table_size):
        key_str = str(key)
        hash_value = 0

        for i, digit in enumerate(key_str):
            if i % 2 != 0:  # Extraia apenas os dígitos ímpares
                hash_value += int(digit)

        return hash_value % table_size

    def getNumberOfCollisions(self):
        return self.__numberOfCollisions

    def countAddressesByNumberOfCities(self):
        pass
