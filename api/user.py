from flask import jsonify, request, abort
from werkzeug.security import generate_password_hash, check_password_hash
from . import api_bp
from models import db, User

@api_bp.route('/api/users', methods=['POST'])
def create_user():
    if not request.json or not 'username' in request.json or not 'password' in request.json:
        abort(400)
    
    hashed_password = generate_password_hash(request.json['password'], method='sha256')
    
    user = User(
        username=request.json['username'],
        password=hashed_password,
        email=request.json.get('email', '')
    )
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    }), 201

@api_bp.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    })

@api_bp.route('/api/users/login', methods=['POST'])
def login_user():
    if not request.json or not 'username' in request.json or not 'password' in request.json:
        abort(400)
    
    user = User.query.filter_by(username=request.json['username']).first()
    
    if user and check_password_hash(user.password, request.json['password']):
        return jsonify({
            'message': 'Login successful!',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        })
    else:
        abort(401)

# Other user management endpoints (like update, delete) can be added similarly.
