from pymongo import MongoClient
import certifi
from datetime import datetime
import validators

def is_valid_id(id):
    return id.isalnum() and id.islower()

def is_valid_website(url):
    return validators.url(url)

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def list_all_ysws():
    client = MongoClient("mongodb+srv://admin:soote@hackclub-ysws.cy7fd.mongodb.net/?retryWrites=true&w=majority&appName=HackClub-YSWS", tlsCAFile=certifi.where())

    db = client["ysws"]
    collection = db["ysws"]

    ysws = list(collection.find())

    for index in range(len(list(collection.find()))):
        del ysws[index]["_id"]
        del ysws[index]["tagline"]
        del ysws[index]["you_ship"]
        del ysws[index]["we_ship"]
        del ysws[index]["description"]
        

    return ysws

def list_done_ysws():
    client = MongoClient("mongodb+srv://admin:soote@hackclub-ysws.cy7fd.mongodb.net/?retryWrites=true&w=majority&appName=HackClub-YSWS", tlsCAFile=certifi.where())

    db = client["ysws"]
    collection = db["ysws"]

    ysws = []

    for index in range(len(list(collection.find()))):
        if collection.find()[index]["completed"]:
            ysws.append(collection.find()[index])

    return ysws

def list_ysws_by_id(id):
    client = MongoClient("mongodb+srv://admin:soote@hackclub-ysws.cy7fd.mongodb.net/?retryWrites=true&w=majority&appName=HackClub-YSWS", tlsCAFile=certifi.where())

    db = client["ysws"]
    collection = db["ysws"]

    ysws = None

    for index in range(len(list(collection.find()))):
        if collection.find()[index]["id"] == id:
            ysws = collection.find()[index]
            del ysws["_id"]

    return ysws

def modify_ysws(input):
    client = MongoClient("mongodb+srv://admin:soote@hackclub-ysws.cy7fd.mongodb.net/?retryWrites=true&w=majority&appName=HackClub-YSWS", tlsCAFile=certifi.where())

    db = client["ysws"]
    collection = db["ysws"]

    if not validate_entry(input["ysws"]):
        return "invalid entry! please post again!"
    
    if input["type"] == "add":
        collection.insert_one(input["ysws"])
        return "add success!"
    elif input["type"] == "modify":
        for index in range(len(list(collection.find()))):
            if collection.find()[index]["id"] == input["ysws"]["id"]:
                collection.update_one({"id": input["ysws"]})
                return "modify success!"
    elif input["type"] == "delete":
        for index in range(len(list(collection.find()))):
            if collection.find()[index]["id"] == input["ysws"]["id"]:
                collection.delete_one({"id": input["ysws"]["id"]})
                return "delete success!"
    
def validate_entry(data):
    try:
        if "id" not in data.keys() and type(data["id"]) != str:
            print("id error")
            return False
        elif not is_valid_id(data["id"]):
            print("id error")
            return False
        
        if "name" not in data.keys() and type(data["name"]) != str:
            print("name error")
            return False
        
        if "tagline" not in data.keys() and type(data["tagline"]) != str:
            print("tagline error")
            return False
        
        if "banner" not in data.keys() and type(data["banner"]) != str:
            print("banner error")
            return False
        
        if "you_ship" not in data.keys() and type(data["you_ship"]) != str:
            print("ys error")
            return False
        
        if "we_ship" not in data.keys() and type(data["we_ship"]) != str:
            print("ws error")
            return False
        
        if "website" not in data.keys() and type(data["website"]) != str:
            print("website error")
            return False
        elif not is_valid_website(data["website"]):
            print("website error")
            return False

        if "channel" not in data.keys() and type(data["website"]) != str:
            print("website error")
            return False
        elif not is_valid_website(data["website"]):
            print("website error")
            return False    

        if "completed" not in data.keys() and type(data["completed"]) != bool:
            print("completed error")
            return False
        
        if "description" not in data.keys() and type(data["description"]) != bool:
            print("description error")
            return False
        
        if "end" not in data.keys() and type(data["end"]) != str:
            print("end error")
            return False
        elif not is_valid_date(data["end"]):
            if data["end"] != "never":
                print("end error")
                return False
        
        if len(data.keys()) != 11:
            print("length error")
            return False

        return True
    except:
        return False

if __name__ == "__main__":
    print(list_done_ysws())