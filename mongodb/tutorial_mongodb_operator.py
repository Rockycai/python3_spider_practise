import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

count = collection.find().count()
print(count)

# 按条件统计
count = collection.find({'age': 25}).count()
print(count)

# 排序 ASCENDING 生序, DESCENDING 降序
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

# 偏移1个元素
results = collection.find().sort('name', pymongo.ASCENDING).skip(1)
print([result['name'] for result in results])

# 返回结果个数
results = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(1)
print([result['name'] for result in results])

# 更新数据
condition = {'name': 'wenlinux'}
student = collection.find_one(condition)
student['age'] = 27
result = collection.update(condition, student)
print(result)

result = collection.remove({'name': 'wenlinux'})
print(result)
