from pymongo import MongoClient
from random import choice
from time import perf_counter
from string import ascii_uppercase, digits

def id_generator(size=20, chars=ascii_uppercase + digits):
    return ''.join(choice(chars) for _ in range(size))

N = int(input("podaj n: "))
start = perf_counter()

client = MongoClient("10.100.100.210")
mydbMongo = client['mongo1']
stringsMongo = mydbMongo.strings

stringsMongo.drop()

randomDict = {}
while len(randomDict) < (10 ** N):
    randomDict[id_generator()] = 1

i = 0
items = []
for elem in randomDict:
    items.append((i, elem))
    i += 1

stringsList = [{"id": i[0], "name": i[1]} for i in items]

result = stringsMongo.insert_many(stringsList)

stop = perf_counter()

print("dodano: " + str(len(result.inserted_ids)) + " rekordow")
print("Czas: " + str(stop - start) + " s")
