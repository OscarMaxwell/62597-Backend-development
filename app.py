from flask import Flask, render_template, request
from flask_graphql import GraphQLView
from schema import schema
from pymongo import MongoClient
import pprint

app = Flask(__name__)

client = MongoClient(port=27017)
db = client.webshop


@app.route("/")
def hello_world():
    return "<p>Hello, World!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</p>"


app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


@app.route("/data", methods=["GET", "POST"])
def data():
    data = []
    json_data = request.get_json()

    if request.method == "POST":
        db.deliveryInfo.insert_one(json_data)
    elif request.method == "GET":
        return str(data.append(db.deliveryInfo.find()))


@app.route("/test")
def test():
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
