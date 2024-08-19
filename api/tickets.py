from flask import jsonify, request, abort
from . import api_bp
from models import db, Ticket

@api_bp.route('/api/tickets', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([{
        'id': t.id,
        'event_name': t.event_name,
        'purchaser_name': t.purchaser_name,
        'amount': t.amount,
        'status': t.status
    } for t in tickets])

@api_bp.route('/api/tickets/<int:id>', methods=['GET'])
def get_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    return jsonify({
        'id': ticket.id,
        'event_name': ticket.event_name,
        'purchaser_name': ticket.purchaser_name,
        'amount': ticket.amount,
        'status': ticket.status
    })

@api_bp.route('/api/tickets', methods=['POST'])
def create_ticket():
    if not request.json or not 'event_name' in request.json:
        abort(400)
    
    ticket = Ticket(
        event_name=request.json['event_name'],
        purchaser_name=request.json.get('purchaser_name', ''),
        amount=request.json.get('amount', 0.0),
        status='Pending'
    )
    db.session.add(ticket)
    db.session.commit()
    
    return jsonify({
        'id': ticket.id,
        'event_name': ticket.event_name,
        'purchaser_name': ticket.purchaser_name,
        'amount': ticket.amount,
        'status': ticket.status
    }), 201

@api_bp.route('/api/tickets/<int:id>', methods=['PUT'])
def update_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    
    if not request.json:
        abort(400)
    
    ticket.event_name = request.json.get('event_name', ticket.event_name)
    ticket.purchaser_name = request.json.get('purchaser_name', ticket.purchaser_name)
    ticket.amount = request.json.get('amount', ticket.amount)
    ticket.status = request.json.get('status', ticket.status)
    
    db.session.commit()
    
    return jsonify({
        'id': ticket.id,
        'event_name': ticket.event_name,
        'purchaser_name': ticket.purchaser_name,
        'amount': ticket.amount,
        'status': ticket.status
    })

@api_bp.route('/api/tickets/<int:id>', methods=['DELETE'])
def delete_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    
    return jsonify({'result': True})
