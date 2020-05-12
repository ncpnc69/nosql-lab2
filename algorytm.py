from pymongo import MongoClient
from time import perf_counter
from random import choice

start = perf_counter()

client = MongoClient("10.100.100.210")
mydbMongo = client['mydb1']
stringsMongo = mydbMongo.strings

stringsCopy = mydbMongo.stringsCopy
stringsCopy.drop()

print("Pobieranie danych z mongoDb1")
fetchStart = perf_counter()
result1 = stringsMongo.find()
fetchEnd = perf_counter()
print("Czas pobierania: " + str(fetchEnd - fetchStart) + " s")

i = 0
count = stringsMongo.count_documents({})
resultList = [item for item in result1]

while i < count:
    randomString = choice(resultList)
    result = stringsCopy.find_one({'name': randomString['name']})
    if type(result) == type(None):
        stringsCopy.insert_one({'id': randomString['id'], 'name': randomString['name']})
        i += 1

stop = perf_counter()
print("Czas wykonania: " + str(stop - start) + " s")
