
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

def insertRandom(cities, hashTable, method):
    if(method == "extraction"):
        for city in cities:
            if(random.randint(0,1) == 0):
                hashTable.insertWithExtraction(city, "Value: " + city)
        return hashTable.getNumberOfCollisions(), hashTable.countAddresssWithCities()
    if(method == "division"):
        for city in cities:
            if(random.randint(0,1) == 0):
                hashTable.insertWithDivision(city, "Value: " + city)
        return hashTable.getNumberOfCollisions(), hashTable.countAddresssWithCities()
    
def calculateAverageCollisions(listCollisions):
    average = 0
    for number in listCollisions:
        average += number
    return average/len(listCollisions)

def calculateAverageAddresssWithCitie(listOfLists):
    num_fields = len(listOfLists[0])
    averages = [0] * num_fields

    # Somar os valores de cada campo em todas as sublistas
    for sublist in listOfLists:
        for i, value in enumerate(sublist):
            averages[i] += value

    # Calcular a média de cada campo
    num_sublists = len(listOfLists)
    for i in range(num_fields):
        averages[i] /= num_sublists

    return averages

cities = getFileData("cidades.txt")
hashTable = HashTable()

listCollisions = []
listNumberOfAssociatedCities = [] 
interations = 1000

for i in range(interations):
    collisions, numberofAssociatedCities = insertRandom(cities, hashTable, "division")
    listCollisions.append(collisions)
    listNumberOfAssociatedCities.append(numberofAssociatedCities)
    hashTable.reset()
print(calculateAverageCollisions(listCollisions))
print(calculateAverageAddresssWithCitie(listNumberOfAssociatedCities))


listCollisions = []
listNumberOfAssociatedCities = [] 

for i in range(interations):
    collisions, numberofAssociatedCities = insertRandom(cities, hashTable, "extraction")
    listCollisions.append(collisions)
    listNumberOfAssociatedCities.append(numberofAssociatedCities)
    hashTable.reset()
print(calculateAverageCollisions(listCollisions))
print(calculateAverageAddresssWithCitie(listNumberOfAssociatedCities))






