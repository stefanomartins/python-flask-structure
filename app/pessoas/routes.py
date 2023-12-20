from flask import render_template, request, jsonify
from app.pessoas import bp
from app.extensions import db
from app.models.pessoa import Pessoa


@bp.route("/", methods=["GET"])
def index():
    pessoas = Pessoa.query.all()
    pessoas = [{"id": pessoa.id, "nome": pessoa.nome} for pessoa in pessoas]

    return jsonify(pessoas=pessoas)


@bp.route("/<int:id>", methods=["GET"])
def show(id: int):
    pessoa = Pessoa.query.get(id)
    pessoa = {
        "id": pessoa.id,
        "name": pessoa.nome,
        "casa_logradouro": pessoa.casa.logradouro,
        "casa_numero": pessoa.casa.numero,
        "casa_complemento": pessoa.casa.complemento,
        "carros": [
            {
                "carro_placa": carro.placa,
                "carro_marca": carro.marca,
                "carro_modelo": carro.modelo,
            }
            for carro in pessoa.carros
        ],
    }
    return jsonify(pessoa)


@bp.route("/add", methods=["POST"])
def create():
    if request.is_json:
        json_data = request.get_json()
        nome = json_data.get("nome")
        casa_id = json_data.get("casa_id")
        pessoa = Pessoa(nome=nome, casa_id=casa_id)
        db.session.add(pessoa)
        db.session.commit()
        return jsonify({"message": "Pessoa adicionada com sucesso."})


@bp.route("/delete/<int:id>", methods=["DELETE"])
def delete(id: int):
    pessoa = Pessoa.query.get(id)
    db.session.delete(pessoa)
    db.session.commit()
    return jsonify({"message": "Pessoa excluída com sucesso."})


@bp.route("/edit/<int:id>", methods=["PUT"])
def edit(id: int):
    if request.is_json:
        json_data = request.get_json()
        pessoa = Pessoa.query.get(id)
        pessoa.nome = json_data.get("nome")
        db.session.commit()
        return jsonify({"message": "Pessoa atualizada com sucesso."})
