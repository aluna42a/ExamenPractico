from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.secret_key = "secretkey123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///credits.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    tasa_interes = db.Column(db.Float, nullable=False)
    plazo = db.Column(db.Integer, nullable=False)
    fecha_otorgamiento = db.Column(db.String(10), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    creditos = Credit.query.all()
    clientes = [c.cliente for c in creditos]
    montos = [c.monto for c in creditos]

    rangos = ['0-999', '1000-4999', '5000-9999', '10000+']
    rango_montos = [0, 0, 0, 0]
    for c in creditos:
        if c.monto < 1000:
            rango_montos[0] += 1
        elif c.monto < 5000:
            rango_montos[1] += 1
        elif c.monto < 10000:
            rango_montos[2] += 1
        else:
            rango_montos[3] += 1

    return render_template('index.html', creditos=creditos, clientes=clientes, montos=montos, rangos=rangos, rango_montos=rango_montos)

@app.route('/add', methods=['GET', 'POST'])
def add_credit():
    if request.method == 'POST':
        cliente_input = request.form['cliente'].strip()
        cliente_normalizado = cliente_input.lower()
        cliente_mostrar = cliente_input.title()
        monto = request.form['monto']
        tasa_interes = request.form['tasa_interes']
        plazo = request.form['plazo']
        fecha_otorgamiento = request.form['fecha_otorgamiento']

        if not cliente_input or not monto or not tasa_interes or not plazo or not fecha_otorgamiento:
            flash("Todos los campos son obligatorios", "error")
            return redirect(url_for('add_credit'))

        existente = Credit.query.filter(func.lower(Credit.cliente) == cliente_normalizado).first()
        if existente:
            flash("Este cliente ya tiene un crédito activo", "active_client")
        
        nuevo_credit = Credit(
            cliente=cliente_mostrar,
            monto=float(monto),
            tasa_interes=float(tasa_interes),
            plazo=int(plazo),
            fecha_otorgamiento=fecha_otorgamiento
        )
        db.session.add(nuevo_credit)
        db.session.commit()
        flash("Crédito agregado correctamente", "success")
        return redirect(url_for('index'))

    return render_template('form.html', credit=None, action="Agregar")

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_credit(id):
    credit = Credit.query.get_or_404(id)
    if request.method == 'POST':
        credit.cliente = request.form['cliente'].title()
        credit.monto = float(request.form['monto'])
        credit.tasa_interes = float(request.form['tasa_interes'])
        credit.plazo = int(request.form['plazo'])
        credit.fecha_otorgamiento = request.form['fecha_otorgamiento']
        db.session.commit()
        flash("Crédito actualizado correctamente", "success")
        return redirect(url_for('index'))
    return render_template('form.html', credit=credit, action="Editar")

@app.route('/delete/<int:id>', methods=['POST'])
def delete_credit(id):
    credit = Credit.query.get_or_404(id)
    db.session.delete(credit)
    db.session.commit()
    flash("Crédito eliminado correctamente", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
