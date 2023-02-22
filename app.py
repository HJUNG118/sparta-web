from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbhaejeong



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/api/list', methods=['POST'])
def memo_list():
    title_receive = request.form['title_give']
    text_receive = request.form['text_give']
    doc = (
        {'title': title_receive,
         'text': text_receive}
    )
    db.memos.insert_one(doc)
    return jsonify({'result': 'success'})

@app.route('/api/get', methods=['GET'])
def memo_up():
    memos = list(db.memos.find({}, {'_id':False}))
    return jsonify({'result': 'success', 'memos': memos})


@app.route('/api/modify', methods=['POST'])
def memo_modify():
     origin = request.form['origin_title']
    #  원래 제목 데이터를 받아오지 못함
     new_title = request.form['update_title']
     new_text = request.form['update_text']
     db.memos.update_one({'title':origin}, {'$set': {'text': new_text, 'title': new_title}},)

     return jsonify({'result': 'success'})


@app.route('/api/delete', methods=['POST'])
def memo_delete():
    title_receive = request.form['title_give']
    db.memos.delete_one({'title':title_receive})

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


first1
first2
second1