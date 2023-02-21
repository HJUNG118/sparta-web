from pymongo import MongoClient
import random

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('mongodb://test:test@15.164.166.98', 27017)
db = client.sparta



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/api/list', methods=['POST'])
def memo_save():
    title_receive = request.form['title_give']
    text_receive = request.form['text_give']
    # num = random.randrange(1,100)
    # 숫자를 늘릴 방법이 필요하다
    num = title_receive[0:1]
    doc = ({'title': title_receive,'text': text_receive, 'num': num})
    db.memos.insert_one(doc)
    return jsonify({'result': 'success'})

@app.route('/api/get', methods=['GET'])
def memo_up():
    memos = list(db.memos.find({},{'_id':False}))
    return jsonify({'result': 'success', 'memos': memos})


@app.route('/api/modify', methods=['POST'])
def memo_modify():
     origin = request.form['origin']
     title = request.form['update_title']
     text = request.form['update_text']
     db.memos.update_one({'num':origin}, {'$set':{'title':title, 'text':text}})
     return jsonify({'result': 'success'})


@app.route('/api/delete', methods=['POST'])
def memo_delete():
    title_receive = request.form['title_give']
    db.memos.delete_one({'title':title_receive})

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


