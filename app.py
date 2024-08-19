from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Ticket
from forms import TicketForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
db.init_app(app)

@app.route('/')
def index():
    tickets = Ticket.query.all()
    return render_template('ticket_list.html', tickets=tickets)

@app.route('/ticket/new', methods=['GET', 'POST'])
def new_ticket():
    form = TicketForm()
    if form.validate_on_submit():
        ticket = Ticket(
            event_name=form.event_name.data,
            purchaser_name=form.purchaser_name.data,
            amount=form.amount.data,
            status='Pending'
        )
        db.session.add(ticket)
        db.session.commit()
        flash('Ticket created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('ticket_detail.html', form=form)

@app.route('/ticket/<int:id>/remit', methods=['POST'])
def remit_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    ticket.status = 'Remitted'
    db.session.commit()
    flash(f'Ticket for {ticket.event_name} remitted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
