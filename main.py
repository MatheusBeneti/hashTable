
from HashTable import HashTable

def getFileData(filename):
    cities = []
    with open(filename, 'r') as file:
        for line in file:
            # Remove o caractere de nova linha (\n) de cada linha
            line = line.rstrip('\n')
            cities.append(line)
    return cities
    
cities = getFileData("cidades.txt")
hashTable = HashTable()

for city in cities:
    hashTable.insertWithDivision(city, "Value: " + city)
print("Número de colisões usando método da divisão: ", hashTable.getNumberOfCollisions())
hashTable.exportToFile("hashWithDivision.txt")
print(hashTable.countAddresssWithCities())

hashTable2 = HashTable()

for city in cities:
    hashTable2.insertWithExtration(city, "Value: " + city)
print("Número de colisões usando método da extração: ", hashTable2.getNumberOfCollisions())
hashTable2.exportToFile("hashWithExtration.txt")
print(hashTable2.countAddresssWithCities())






