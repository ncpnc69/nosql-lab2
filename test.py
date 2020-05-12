from pymongo import MongoClient
from time import perf_counter

start = perf_counter()

client1 = MongoClient("10.100.100.210")
mydbMongo1 = client1['mongo1']

client2 = MongoClient("10.100.100.220")
mydbMongo2 = client2['mongo2']

fetchStart = perf_counter()

stringsMongo1 = mydbMongo1.strings
stringsMongo2 = mydbMongo2.strings

stringsMongo2.drop()

result1 = stringsMongo1.find()
fetchEnd = perf_counter()

print("Czas pobierania: " + str(fetchEnd - fetchStart) + " s")

stringList = [{"id": string["id"], "name": string["name"]} for string in result1]

result = stringsMongo2.insert_many(stringList)

insertEnd = perf_counter()
print("dodano" + str(len(result.inserted_ids)) + " rekordow, czas: " + str(insertEnd - fetchEnd) + " s")

stop = perf_counter()
print("Czas wykonania: " + str(stop - start) + " s")
