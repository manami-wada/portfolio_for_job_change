from flask import Flask, jsonify
import random
import os

 

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False
os.environ["FLASK_APP"]="app.py"
FLASK_APP=app.py
 

@app.route('/fortune', methods=['GET'])
def fortune():
    fortunes = [
      '大吉',
      '小吉',
      '吉',
      '凶',
      '大凶'
    ]

 

    return jsonify({
        'status':'OK',
        'data':random.choice(fortunes)
    }), 200
