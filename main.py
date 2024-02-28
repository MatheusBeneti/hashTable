
from HashTable import HashTable
import random

def getFileData(filename):
    cities = []
    with open(filename, 'r') as file:
        for line in file:
            # Remove o caractere de nova linha (\n) de cada linha
            line = line.rstrip('\n')
            cities.append(line)
    return cities

def insertCities(cities, hashTable, method):
    if(method == "extraction"):
        for city in cities:
                hashTable.insertWithExtraction(city, "Value: " + city)
        return hashTable.getNumberOfCollisions(), hashTable.countAddresssWithCities()
    if(method == "division"):
        for city in cities:
                hashTable.insertWithDivision(city, "Value: " + city)
        return hashTable.getNumberOfCollisions(), hashTable.countAddresssWithCities()



cities = getFileData("cidades.txt")
hashTable = HashTable()
iterations = 1000

bestSize = None
fewerCollisions = float('inf')  
fewerEmptyAddresses = float('inf')  
bestPlacedAddresses = None

for i in range(iterations):
    hashTableSize = i + 1
    hashTable.reset(hashTableSize)
    collisions, numberofAssociatedCities = insertCities(cities, hashTable, "division")
    emptyAddresses = hashTable.countAddresssWithCities()[0]

    if collisions < fewerCollisions or (collisions == fewerCollisions and emptyAddresses < fewerEmptyAddresses):
        fewerCollisions = collisions
        fewerEmptyAddresses = emptyAddresses
        bestSize = hashTableSize
        bestPlacedAddresses = hashTable.countAddresssWithCities()

print(bestSize, fewerCollisions, fewerEmptyAddresses, bestPlacedAddresses)
print("division: finish")

bestSize = None
fewerCollisions = float('inf')  
fewerEmptyAddresses = float('inf')  
bestPlacedAddresses = None

for i in range(iterations):
    hashTableSize = i + 1
    hashTable.reset(hashTableSize)
    collisions, numberofAssociatedCities = insertCities(cities, hashTable, "extraction")
    emptyAddresses = hashTable.countAddresssWithCities()[0]

    if collisions < fewerCollisions or (collisions == fewerCollisions and emptyAddresses < fewerEmptyAddresses):
        fewerCollisions = collisions
        fewerEmptyAddresses = emptyAddresses
        bestSize = hashTableSize
        bestPlacedAddresses = hashTable.countAddresssWithCities()

print(bestSize, fewerCollisions, fewerEmptyAddresses, bestPlacedAddresses)
print("finish")










