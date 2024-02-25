file = "cidades.txt"
arquivo = open(file, 'r')

cities = []
with open(file, 'r') as arquivo:
    for line in arquivo:
        # Remove o caractere de nova linha (\n) de cada linha
        line = line.rstrip('\n')
        cities.append(line)

class HashTable:
    def __init__(self):
        self.__table = [None] * 10 
    
    def insert(self, key, value):
        hashedKey = self.__hash(key)

        positionToAllocate = self.__getPositionToAllocate(hashedKey)

        self.__allocate(positionToAllocate, value)

    def __hash(self, string):
        hash_value = 0  
        for char in string: 
            hash_value += ord(char)  
        return hash_value
    
    def __getPositionToAllocate(self, hashedKey):
        return hashedKey % len(self.__table) 

    def __allocate(self, position, value):
        self.__table[position] = value

    # Pegar um valor basendo na chave
    def getValue(self, key):
        hashedKey = self.__hash(key)
        position = self.__getPositionToAllocate(hashedKey)
        return self.__table[position]

hashTable = HashTable()

for city in cities:
    hashTable.insert(city, "Cidade de " + city)

for city in cities:
    print(hashTable.getValue(city))




def digit_extraction_hash(key, table_size):
    key_str = str(key)
    hash_value = 0

    for i, digit in enumerate(key_str):
        if i % 2 != 0:  # Extraia apenas os dígitos ímpares
            hash_value += int(digit)

    return hash_value % table_size

# Testando a função
key = 1234567890
table_size = 10
print(digit_extraction_hash(key, table_size))  # Saída: 2

