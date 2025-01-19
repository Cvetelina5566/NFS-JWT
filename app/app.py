from flask import Flask,request, jsonify
import os
import jwt

app = Flask(__name__)

NFS_PATH = os.getenv("NFS_PATH", "/nfs")
SECRET_KEY = 'mysecretkey'

def authenticate_token():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Token is missing!"}), 403
    try:
        token = token.split(" ")[1]
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except Exception as e:
        return jsonify({"message": "Token is invalid!"}), 403

@app.route('/file/upload', methods=['POST'])
def upload_file():
    user = authenticate_token()
    if isinstance(user, tuple):
        return user
    
    file = request.files['file']
    file_path = os.path.join(NFS_PATH, file.filename)
    file.save(file_path)
    return jsonify({"message": "File uploaded successfully!"}), 201

@app.route('/file/<file_id>', methods=['GET'])
def get_file(file_id):
    user = authenticate_token()
    if isinstance(user, tuple):
        return user
    
    file_path = os.path.join(NFS_PATH, file_id)
    if not os.path.exists(file_path):
        return jsonify({"message": "File not found!"}), 404
    
    with open(file_path, 'rb') as file:
        content = file.read()
    return content

@app.route('/file/<file_id>', methods=['PUT'])
def update_file(file_id):
    user = authenticate_token()
    if isinstance(user, tuple):
        return user
    
    file = request.files['file']
    file_path = os.path.join(NFS_PATH, file_id)
    if not os.path.exists(file_path):
        return jsonify({"message": "File not found!"}), 404
    
    file.save(file_path)
    return jsonify({"message": "File updated successfully!"}), 200

@app.route('/file/<file_id>', methods=['DELETE'])
def delete_file(file_id):
    user = authenticate_token()
    if isinstance(user, tuple):
        return user
    
    file_path = os.path.join(NFS_PATH, file_id)
    if not os.path.exists(file_path):
        return jsonify({"message": "File not found!"}), 404
    
    os.remove(file_path)
    return jsonify({"message": "File deleted successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
