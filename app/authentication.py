from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .models import User
from . import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

# Other authentication endpoints (register, logout, etc.)
