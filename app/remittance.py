from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Ticket, User
from . import db

bp = Blueprint('remittance', __name__)

@bp.route('/remit', methods=['POST'])
@jwt_required()
def remit():
    user_id = get_jwt_identity()
    data = request.json
    ticket = Ticket(user_id=user_id, event_name=data['event_name'])
    db.session.add(ticket)
    db.session.commit()
    return jsonify({"msg": "Remittance successful", "ticket_id": ticket.id}), 201

# Other remittance endpoints
