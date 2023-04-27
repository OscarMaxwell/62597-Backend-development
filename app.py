from flask import Flask, render_template, request
# from flask_cors import CORS
from flask_graphql import GraphQLView
from pymongo import MongoClient

from schema import schema

app = Flask(__name__)
# enable CORS for all flask routes
# CORS(app)

# access the database
client = MongoClient(port=27017)
db = client.webshop


@app.route("/")
def hello_world():
    one = db.deliveryInfo.find()
    print(one)
    return "<p>Hello, World!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</p>" + " <p>" + one + "</p>"


app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


@app.route("/data1", methods=["GET", "POST"])
def data1():
    data = []
    json_data = request.get_json()

    if request.method == "POST":
        db.deliveryInfo.insert_one(json_data)
    elif request.method == "GET":
        if str(data.append(db.deliveryInfo.find())) == "None":
            return "No entries"
        else:
            return str(data.append(db.deliveryInfo.find()))


@app.route("/data", methods=["POST"])
def data():
    response = request.get_json()
    db.deliveryInfo.insert_one(response)
    return "Data added successfully"


@app.route("/test")
def test():
    print("test")
    deliveryInfo = db.deliveryInfo

    # Insert a new post
    # post = {"author": "Mike",
    #         "text": "My first blog post!",
    #         "tags": ["mongodb", "python", "pymongo"]}

    # deliveryInfo.insert_one(post)

    # for post in deliveryInfo.find():

    # Retrieve all posts
    posts = deliveryInfo.find()

    # Display all posts
    response = "<h1>All Posts</h1>"
    i = 1
    for post in posts:
        response += f"<h2>Item {i}</h2>"
        response += "<div>"
        for key, value in post.items():
            response += f"<p><strong>{key}:</strong> {value}</p>"
        response += "</div>"
        i += 1
    return response


@app.route("/hello")
def hello():
    db = client['test-database']
    collection = db['test-collection']

    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"]}

    posts = db.posts

    post_id = posts.insert_one(post).inserted_id

    return "1234: " + str(post_id) + "Author: " + post["author"] + "Text: " + post["text"] + "Tags: " + post["tags"][0] + ", " + post["tags"][1] + ", " + post["tags"][2]
