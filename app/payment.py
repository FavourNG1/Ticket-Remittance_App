from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models import Payment, Ticket
from . import db

bp = Blueprint('payment', __name__)

@bp.route('/pay', methods=['POST'])
@jwt_required()
def pay():
    data = request.json
    payment = Payment(ticket_id=data['ticket_id'], amount=data['amount'], status='Pending')
    db.session.add(payment)
    db.session.commit()
    # Integrate with payment gateway here
    payment.status = 'Completed'
    db.session.commit()
    return jsonify({"msg": "Payment successful", "payment_id": payment.id}), 200

# Other payment endpoints
