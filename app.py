#
# @author Victor Sales
#

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
    
@app.route('/api/get_user/<int:id>', methods=['GET'])
def get_user(id):
    
    try:
        user = Users.get_by_id(id)
        return jsonify({
            'id': user.id,
            'name': user.name,
            'password': user.password,
            'email': user.email
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/update_user/<int:id>', methods=['PUT'])
def update_upser(id):
    
    updated_data = request.get_json()
    try:
        user = Users.get_by_id(id)
        user.name = updated_data.get('name', user.name) #Caso não tiver sido passado nenhum valor, manterá o valor presente no banco de dados
        user.password = updated_data.get('password', user.password)
        user.email = updated_data.get('email', user.email)
        user.save()
        return jsonify({'message':'User updated successfully'}),200
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/create_user', methods=['POST'])
def create_user():
    new_user = request.get_json()

    try:
        user_created = Users.create(
            id = new_user.get('id'),
            name = new_user.get('name'),
            password = new_user.get('password'),
            email = new_user.get('email')
        )
            
        return jsonify({'id': user_created.id, 'email': user_created.email}), 200
    except Exception as e:
        return jsonify({'error': str(e)}),400
        
@app.route('/api/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    
    try:
        Users.delete_by_id(id)
        return jsonify({'message':'User deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}),400


if __name__ == '__main__':
    app.run(debug=True)
