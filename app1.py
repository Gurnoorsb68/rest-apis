from flask import Flask, request

app1 = Flask(__name__)  #app1 is also the FILE NAME

stores = [                  #Json is like python dictionary but all data need to be string
    {
        "name" : "MAXI",
        "items" : [
            {
                "name" : "chair",
                "price" : 1200
            },
            {
                "name" : "table",
                "price" : 2400
            }
        ]
    },
    {
        "name" : "DOLLARAMA",
        "items" : [
            {
                "name" : "frypan",
                "price" : 500
            },
            {
                "name" : "chocolate",
                "price" : 200
            }
        ]
    },
    {
        "name" : "kfc",
        "items" : [
            {
                "name" : "chair",
                "price" : 1200
            },
            {
                "name" : "table",
                "price" : 2400
            }
        ]
    }
]

@app1.get("/store")     #OUR FIRST FLASK ROUTE with endpoint /store
def get_stores():
    return {"stores are" : stores} #returninn a python dictionary, flask automatically turn it to json format

@app1.post("/store")
def create_store_new():
    request_new_data = request.get_json()   #now request_new_data is a dictionary with the json format which was recieved
    add_store = {"name" : request_new_data["name"], "items" : request_new_data["items"]}
    stores.append(add_store)
    print(add_store)    #testing on jenkins, rome thiis afterwardss
    return add_store, 201   # return code 201 means accepted the data to create the store

@app1.post("/store/<string:name>/item")     #in name give pass name of the store in postman
def create_item(name):
    request_new_data = request.get_json()   #have the data from postman
    for x in stores:
        if x["name"] == name:
            new_itm = {"name" : request_new_data["name"], "price" : request_new_data["price"]}
            x["items"].append(new_itm)
            return  new_itm, 201
        return  {"message" : "missing store"} , 404

@app1.get("/store/<string:name>")   #API to get perticular store name
def get_store_info(name):
    for x in stores:
        if x["name"] == name:
            return  x
        return  {"message" : "missing store"} , 404

@app1.get("/store/<string:name>/itemdetails")   #API to get Items of particulaar store
def get_item(name):
    for x in stores:
        if x["name"] == name:
            return  {"items" : x["items"]}  # returning dictionary is better, u could have also done x["items"]
        return  {"message" : "missing store"} , 404

app1.run()

