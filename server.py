import os
from flask import Flask, send_from_directory, render_template, redirect, jsonify, request
import random 

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/random', methods=['GET','POST'])
def get_randint():
    if request.method == 'GET':
        return jsonify({
            'randint': random.randint(1,100),
            'type': "GET"
        }), 200
    elif request.method == 'POST':
        return jsonify({
            'randint': random.randint(1,100),
            'type': "POST"
        }), 200


@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')

if __name__ == "__main__":
    app.run(port=port)
