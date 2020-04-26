import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

student1 = {
    'id': '20200425',
    'name': 'wenlinux',
    'age': 25,
    'gander': 'male'
}

student2 = {
    'id': '20200425',
    'name': 'ellia',
    'age': 25,
    'gander': 'female'
}

result = collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)