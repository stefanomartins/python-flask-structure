from flask import request, jsonify
from app.carros import bp
from app.extensions import db
from app.models.carro import Carro

@bp.route('/', methods=['GET'])
def index():
    carros = Carro.query.all()
    data = []
    for carro in carros:
        carro_data = {
            'placa': carro.placa,
            'marca': carro.marca,
            'modelo': carro.modelo,
            'pessoas': [
                {'id': pessoa.id, 'nome': pessoa.nome} for pessoa in carro.pessoas
            ]
        }
        data.append(carro_data)

    return jsonify(carros=data)
