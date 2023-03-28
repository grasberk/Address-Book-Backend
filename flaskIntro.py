from flask import Flask, request
from models.people import People
from flask_cors import CORS
from asyncio import sleep
import json



app = Flask(__name__)
CORS(app)


@app.route("/")
def main():
    c=[]
    people=People.objects().all()
    for person in people:
        l=person.tojson()
        c.append(l)
    return c 

@app.route("/test")
def test():
    return "Hello from the backend"



# #TODO: CRUD operations
# #retrieve
@app.route("/people/<int:id>")
def show(id): 
    # await sleep(3)
    person=People.objects(id=id)
    if person:
        return person.tojson()
    else:
     return {"name": "Alan"}
    
#update
@app.route('/person/edit/<int:id>', methods=['PUT'])
def edit(id):
    person=People.objects(id=id).get()
    if person:
        req_data=request.get_json()
        person.name=req_data["name"]
        person.age=req_data["age"]
        person.img=req_data["img"]
        person.phone_number=req_data["phone_number"]
        person.save()
        return person.tojson()
    else:
        return "id not found"
    

#create
def max_id():
    biggest=0
    people=People.objects().all()
    for person in people:
        if biggest<person.id:
            biggest=person.id
    return biggest
            

        
@app.route('/person/create', methods=['POST'])
def create():

    req_data=request.get_json()
    newid=max_id()+1
    newperson=People(id=newid,name=req_data["name"],age=req_data["age"],img=req_data["img"],phone_number=req_data["phone_number"])
    newperson.save()
    return newperson.tojson()
    


#delete
@app.route('/person/delete/<int:id>', methods=['DELETE'])
def delete(id):
    person=People.objects(id=id)
    if person:
        person.delete()
        return main()
    else:
        return "id not found"
    
@app.route('/reset', methods=['PUT'])
def reset():
    for person in People.objects:
        person.delete()
    file1=open("models/seedData.json",'r')
    s=file1.read()
    seed_data=json.loads(s)
    
    for person in seed_data: 
         addperson=People(id=person["_id"],name=person["name"],age=person["age"],img=person["img"],phone_number=person["phone_number"])
         addperson.save()
    

    return "successful"
    
    

        

    
    

    



    







