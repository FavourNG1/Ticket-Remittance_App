from flask import jsonify, request, abort
from . import api_bp
from models import db, Payment

@api_bp.route('/api/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{
        'id': p.id,
        'ticket_id': p.ticket_id,
        'amount': p.amount,
        'status': p.status,
        'payment_method': p.payment_method,
        'created_at': p.created_at
    } for p in payments])

@api_bp.route('/api/payments/<int:id>', methods=['GET'])
def get_payment(id):
    payment = Payment.query.get_or_404(id)
    return jsonify({
        'id': payment.id,
        'ticket_id': payment.ticket_id,
        'amount': payment.amount,
        'status': payment.status,
        'payment_method': payment.payment_method,
        'created_at': payment.created_at
    })

@api_bp.route('/api/payments', methods=['POST'])
def create_payment():
    if not request.json or not 'ticket_id' in request.json:
        abort(400)
    
    payment = Payment(
        ticket_id=request.json['ticket_id'],
        amount=request.json.get('amount', 0.0),
        status=request.json.get('status', 'Pending'),
        payment_method=request.json.get('payment_method', 'Credit Card')
    )
    db.session.add(payment)
    db.session.commit()
    
    return jsonify({
        'id': payment.id,
        'ticket_id': payment.ticket_id,
        'amount': payment.amount,
        'status': payment.status,
        'payment_method': payment.payment_method,
        'created_at': payment.created_at
    }), 201

@api_bp.route('/api/payments/<int:id>', methods=['PUT'])
def update_payment(id):
    payment = Payment.query.get_or_404(id)
    
    if not request.json:
        abort(400)
    
    payment.amount = request.json.get('amount', payment.amount)
    payment.status = request.json.get('status', payment.status)
    payment.payment_method = request.json.get('payment_method', payment.payment_method)
    
    db.session.commit()
    
    return jsonify({
        'id': payment.id,
        'ticket_id': payment.ticket_id,
        'amount': payment.amount,
        'status': payment.status,
        'payment_method': payment.payment_method,
        'created_at': payment.created_at
    })

@api_bp.route('/api/payments/<int:id>', methods=['DELETE'])
def delete_payment(id):
    payment = Payment.query.get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    
    return jsonify({'result': True})
