from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world(num):
    print(num)
    return 'Hello, World!'

@app.route('/get_time')
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({'time': current_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
