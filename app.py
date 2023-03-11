from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(port=27017)
db = client.webshop


@app.route("/")
def hello_world():
    return "<p>Hello, World!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</p>"

@app.route("/data", method=["GET","POST"])
def data():
    data = []
    json_data = request.get_json()
    

    if request.method == "POST":
       db.deliveryInfo.insert_one(json_data)
    elif request.method == "GET":
        return data.append(db.deliveryInfo.find())
    


# def get_database():
 
#    # Provide the mongodb atlas url to connect python to mongodb using pymongo
#    CONNECTION_STRING = "mongodb://localhost:27017"
 
#    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#    client = MongoClient(CONNECTION_STRING)
 
#    # Create the database for our example (we will use the same database throughout the tutorial
#    return client['user_shopping_list']
  
# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":   
  
#    # Get the database
#    dbname = get_database()
    