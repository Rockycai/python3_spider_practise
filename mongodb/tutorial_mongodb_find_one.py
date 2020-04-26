import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

result = collection.find_one({'name': 'wenlinux'})
# 通过id查找
# result = collection.find_one({'_id': ObjectId('5ea4f0b4654f51d2cd788716')})
# 查找大于20岁的条件
results = collection.find({'age': {'$gt': 20}})
print(result)

for item in results:
    print(item)

results = collection.find({'name': {'$regex': '^w.*'}})
[ print(item) for item in results]