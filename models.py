from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    tasa_interes = db.Column(db.Float, nullable=False)
    plazo = db.Column(db.Integer, nullable=False)
    fecha_otorgamiento = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Credit {self.cliente} - {self.monto}>"
