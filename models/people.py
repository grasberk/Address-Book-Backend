from mongoengine import *
import json

class People(Document):
    id = IntField(primary_key=True)
    name = StringField()
    age = IntField()
    img = StringField()
    phone_number= IntField()


    def tojson(self):
       return json.loads(self.to_json())
