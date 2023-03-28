from mongoengine import connect
mongo_connection_string="mongodb+srv://gavula:natura@charizard.drhnb8f.mongodb.net/?retryWrites=true&w=majority"

connect(db="contacts", host=mongo_connection_string)