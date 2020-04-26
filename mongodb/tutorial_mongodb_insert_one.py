import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

student = {
    'id': '20200426',
    'name': 'Rockycai',
    'age': 25,
    'gender': 'male'
}

result = collection.insert_one(student)
print(result)
print(result.inserted_id)