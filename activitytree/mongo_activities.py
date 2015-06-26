__author__ = 'mario'



from pymongo import MongoClient
from django.conf import settings
_client = MongoClient(settings.MONGO_DB)
_db = _client.protoboard_database
_activities_collection = _db.activities_collection

class Activity:
    @staticmethod
    def get(uri):
        return _activities_collection.find_one({'_id':uri})

