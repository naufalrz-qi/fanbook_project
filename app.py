from flask import Flask, render_template, request, jsonify
# <!-- DATA DIRI -->
# <!-- Nama               : Naufal Rifqi Zuhrian -->
# <!-- ID                 : 4778007 -->
# <!-- Universitas/Kampus : Universitas Bumigora Mataram -->
# <!-- Kelompok/group     : 3 -->
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