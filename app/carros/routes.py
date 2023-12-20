from flask import request, jsonify
from app.carros import bp
from app.extensions import db
from app.models.carro import Carro


@bp.route("/", methods=["GET"])
def index():
    carros = Carro.query.all()
    carros = [
        {"placa": carro.placa, "marca": carro.marca, "modelo": carro.modelo}
        for carro in carros
    ]

    return jsonify(carros=carros)


@bp.route("/<string:placa>", methods=["GET"])
def show(placa: str):
    carro = Carro.query.get(placa)
    carro = {
        "placa": carro.placa,
        "marca": carro.marca,
        "modelo": carro.modelo,
        "motoristas": [
            {"motorista_id": motorista.id, "motorista_nome": motorista.nome}
            for motorista in carro.motoristas
        ],
    }
    return jsonify(carro)

