from django.test import TestCase

# Create your tests here.
import pymongo

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client.NBA_china_spider
collection = db.data

data = [title for title in collection.find()]
print(data[0]['url'])
