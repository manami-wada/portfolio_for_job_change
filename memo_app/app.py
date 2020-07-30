import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Memo

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_memo():
    title=request.args.get('title')
    detail=request.args.get('detail')
    try:
        memo=Memo(
            title=title,
            detail=detail,
        )
        db.session.add(memo)
        db.session.commit()
        return "Memo added. memo id={}".format(memo.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        memos=Memo.query.all()
        return  jsonify([e.serialize() for e in memos])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        memo=Memo.query.filter_by(id=id_).first()
        return jsonify(memo.serialize())
    except Exception as e:
	    return(str(e))

@app.route("/add/form",methods=['GET', 'POST'])
def add_memo_form():
    if request.method == 'POST':
        title=request.form.get('title')
        detail=request.form.get('detail')
        try:
            memo=Memo(
                title=title,
                detail=detail
            )
            db.session.add(memo)
            db.session.commit()
            return "Memo added. memo id={}".format(memo.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")

@app.route("/add/json",methods=['GET', 'POST'])
def add_memo_json():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_memo = Memo(title=data['title'], detail=data['detail'])
            db.session.add(new_memo)
            db.session.commit()
            return {"message": f"memo {new_memo.title} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

if __name__ == '__main__':
    app.run()
