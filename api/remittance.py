from flask import jsonify, request, abort
from . import api_bp
from models import db, Remittance

@api_bp.route('/api/remittances', methods=['GET'])
def get_remittances():
    remittances = Remittance.query.all()
    return jsonify([{
        'id': r.id,
        'ticket_id': r.ticket_id,
        'amount': r.amount,
        'status': r.status,
        'created_at': r.created_at
    } for r in remittances])

@api_bp.route('/api/remittances/<int:id>', methods=['GET'])
def get_remittance(id):
    remittance = Remittance.query.get_or_404(id)
    return jsonify({
        'id': remittance.id,
        'ticket_id': remittance.ticket_id,
        'amount': remittance.amount,
        'status': remittance.status,
        'created_at': remittance.created_at
    })

@api_bp.route('/api/remittances', methods=['POST'])
def create_remittance():
    if not request.json or not 'ticket_id' in request.json:
        abort(400)
    
    remittance = Remittance(
        ticket_id=request.json['ticket_id'],
        amount=request.json.get('amount', 0.0),
        status=request.json.get('status', 'Pending')
    )
    db.session.add(remittance)
    db.session.commit()
    
    return jsonify({
        'id': remittance.id,
        'ticket_id': remittance.ticket_id,
        'amount': remittance.amount,
        'status': remittance.status,
        'created_at': remittance.created_at
    }), 201

@api_bp.route('/api/remittances/<int:id>', methods=['PUT'])
def update_remittance(id):
    remittance = Remittance.query.get_or_404(id)
    
    if not request.json:
        abort(400)
    
    remittance.amount = request.json.get('amount', remittance.amount)
    remittance.status = request.json.get('status', remittance.status)
    
    db.session.commit()
    
    return jsonify({
        'id': remittance.id,
        'ticket_id': remittance.ticket_id,
        'amount': remittance.amount,
        'status': remittance.status,
        'created_at': remittance.created_at
    })

@api_bp.route('/api/remittances/<int:id>', methods=['DELETE'])
def delete_remittance(id):
    remittance = Remittance.query.get_or_404(id)
    db.session.delete(remittance)
    db.session.commit()
    
    return jsonify({'result': True})
