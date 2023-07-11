from flask import Flask, request
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    client = MongoClient('mongodb+srv://irisminami0307:538167294@itamiworld.svqaz2d.mongodb.net/')
    
    db = client['mongodb']
    collection = db['users']
    print(collection)
    
    @app.route('/save', methods=['POST'])
    def save():
        data = request.json
        collection.insert_one(data)
        return 'Success'
    
    return app