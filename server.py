from flask import Flask, jsonify;import threading

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message":"Server Online"})

def run():
    app.run(port=5001)

def server():  
    threading.Thread(target=run).start()
