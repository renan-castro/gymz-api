from flask import Flask, jsonify, request
from database.database import db
from database.user import Users

app = Flask(__name__)

@app.before_request
def before_request():
    if db.is_closed():
        db.connect()

@app.teardown_request
def teardown_request(exception):
    if not db.is_closed():
        db.close()

@app.route('/api/get_users', methods=['GET'])
def get_users():
    try:
        users = Users.select()

        user_list = []
        for user in users:
            user_list.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
            })

        return jsonify(user_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
