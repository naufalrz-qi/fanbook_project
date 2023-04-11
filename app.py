from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# <!-- DATA DIRI -->
# <!-- Nama               : Naufal Rifqi Zuhrian -->
# <!-- ID                 : 4778007 -->
# <!-- Universitas/Kampus : Universitas Bumigora Mataram -->
# <!-- Kelompok/group     : 3 -->


MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)

db = client[DB_NAME]


app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/info',methods=['GET'])
def get_info():
    my_name = request.args.get('my_name')
    print(my_name)
    return jsonify({
        'msg' : 'GET info'
    })
    
@app.route('/info',methods=['POST'])
def post_info():
    my_name = request.form.get('my_name')
    print(my_name)
    return jsonify({
        'msg' : 'POST info'
    })

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)