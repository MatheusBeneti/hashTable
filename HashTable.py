class HashTable:
    def __init__(self):
        self._table = [None] * 853
        self._numberOfCollisions = 0

    def insertWithDivision(self, key, value):
        hashedKey = self._hashDivisionMethod(key)
        positionToAllocate = self._getPositionToAllocate(hashedKey)
        self._allocate(positionToAllocate, key, value)

    def insertWithExtration(self, key, value):
        hashedKey = self._digitExtractionHash(key)
        positionToAllocate = self._getPositionToAllocate(hashedKey)
        self._allocate(positionToAllocate, key, value)

    def _hashDivisionMethod(self, string):
        hash_value = 0
        for char in string:
            hash_value += ord(char)
        return hash_value
    
    def _digitExtractionHash(self, key):
        hash_value = 0

        for i in key:
            if ord(i) % 2 != 0:  # Extraia apenas os dígitos ímpares
                hash_value += ord(i)
        return hash_value

    def _getPositionToAllocate(self, hashedKey):
        return hashedKey % len(self._table)

    def _allocate(self, position, key, value):
        if self._table[position] is None:
            self._table[position] = []
        else:
            if (key, value) not in self._table[position]:  # Verifica se a entrada já existe
                self._numberOfCollisions += 1
        self._table[position].append((key, value))

    def getValues(self, key):
        hashedKey = self._hashDivisionMethod(key)
        position = self._getPositionToAllocate(hashedKey)
        entries = self._table[position]
        if entries is not None:
            for entry in entries:
                if entry[0] == key:
                    return entry[1]
        return None

    def exportToFile(self, filename):
        try:
            with open(filename, 'w') as file:
                for entry in self._table:
                    if entry is not None:
                        line_values = ', '.join([f"{key}:{value}" for key, value in entry])
                        file.write(line_values + '\n')
        except IOError:
            print("Erro ao escrever no arquivo.")

    def reset(self):
        self._table = [None] * 853
        self._numberOfCollisions = 0
        
    def getNumberOfCollisions(self):
        return self._numberOfCollisions

    def countAddresssWithCities(self):
        counts = [0] * 11  # Inicializa uma lista de contagens para 11 categorias (0 a 10+)
        
        for entry in self._table:
            if entry is not None:
                num_cities = len(entry)
                if num_cities >= 10:
                    counts[10] += 1
                else:
                    counts[num_cities] += 1

        return counts
