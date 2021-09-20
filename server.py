from flask import Flask, jsonify;from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message":"Server Online"})

def run():
    app.run(port=5001)

def server():  
    Thread(target=run).start()
