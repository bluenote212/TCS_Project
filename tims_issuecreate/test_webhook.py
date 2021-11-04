from flask import Flask, request
import pymongo
from datetime import datetime

app = Flask(__name__)

@app.route('/rest', methods=['GET', 'POST'])
def hello_world():
    data = request.get_json()
    parameter_dict = request.args.to_dict()
    day = datetime.now()
    
    conn = pymongo.MongoClient("192.168.3.237", 27017)
    db = conn.tcs
    col = db.rest
    
    col.insert_one({
                'data': data,
                'prrameter': parameter_dict,
                'date': day
            })
    
    
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000)
