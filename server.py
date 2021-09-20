from flask import Flask;from threading import Thread

app = Flask()

@app.route('/')
def index():
    return "Server Online"

def run():
    app.run(port=5001)

def server():  
    Thread(target=run).start()