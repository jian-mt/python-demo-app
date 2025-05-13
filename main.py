from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    # 模拟一些处理时间
    time.sleep(random.uniform(0.05, 0.2))
    return jsonify({"message": "Hello World!"})

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    # 模拟数据库查询
    time.sleep(random.uniform(0.1, 0.5))
    return jsonify({"user_id": user_id, "name": f"User {user_id}", "status": "active"})

@app.route('/api/items', methods=['POST'])
def create_item():
    # 模拟创建项目
    time.sleep(random.uniform(0.2, 0.6))
    item = request.json
    item["id"] = random.randint(1000, 9999)
    return jsonify(item), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
