from flask import Flask, render_template, request, redirect, url_for, abort
import mongo_manager
from pymongo import MongoClient
import certifi

app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:soote@hackclub-ysws.cy7fd.mongodb.net/?retryWrites=true&w=majority&appName=HackClub-YSWS", tlsCAFile=certifi.where())

db = client["ysws"]
collection = db["ysws"]

@app.route('/')
def home():
    return "hello world"

@app.route("/api/all")
def all():
    return mongo_manager.list_all_ysws()

@app.route("/api/<id>")
def page(id):
    page_data = collection.find_one({"id": id})
    if not page_data:
        abort(404) 
    return mongo_manager.list_ysws_by_id(id)

@app.route("/api/done")
def done():
    return mongo_manager.list_done_ysws()

@app.route("/api/modify", methods=["POST"])
def modify():
    data = request.json
    return mongo_manager.modify_ysws(data)


@app.route("/api/bulk_add", methods=["POST"])
def add_more():
    data = request.json
    for item in data["ysws"]:
        collection.insert_one(item)
    
    return 'done!'


# if __name__ == '__main__':
#     app.run(debug=True)
