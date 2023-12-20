from flask import request, jsonify
from app.casas import bp
from app.extensions import db
from app.models.casa import Casa


@bp.route("/", methods=["GET"])
def index():
    casas = Casa.query.all()
    data = []

    for casa in casas:
        casa_data = {
            "id": casa.id,
            "logradouro": casa.logradouro,
            "numero": casa.numero,
            "complemento": casa.complemento,
            "residentes": [
                {"id": pessoa.id, "nome": pessoa.nome} for pessoa in casa.residentes
            ],
        }
        data.append(casa_data)

    return jsonify(casas=data)


@bp.route("/<int:id>", methods=["GET"])
def show(id: int):
    casa = Casa.query.get(id)
    casa = {
        "id": casa.id,
        "logradouro": casa.logradouro,
        "numero": casa.numero,
        "complemento": casa.complemento,
        "residentes": [
            {"id": pessoa.id, "nome": pessoa.nome} for pessoa in casa.residentes
        ],
    }
    return jsonify(casa)


@bp.route("/add", methods=["POST"])
def create():
    if request.is_json:
        json_data = request.get_json()
        logradouro = json_data.get("logradouro")
        numero = json_data.get("numero")
        complemento = json_data.get("complemento")
        casa = Casa(logradouro=logradouro, numero=numero, complemento=complemento)
        db.session.add(casa)
        db.session.commit()
        return jsonify({"message": "Casa adicionada com sucesso."})


@bp.route("/edit/<int:id>", methods=["PUT"])
def edit(id: int):
    if request.is_json:
        json_data = request.get_json()
        casa = Casa.query.get(id)
        casa.logradouro = json_data.get("logradouro")
        casa.numero = json_data.get("numero")
        casa.complemento = json_data.get("complemento")
        db.session.commit()
        return jsonify({"message": "Casa atualizada com sucesso."})


@bp.route("/delete/<int:id>", methods=["DELETE"])
def delete(id: int):
    casa = Casa.query.get(id)
    db.session.delete(casa)
    db.session.commit()
    return jsonify({"message": "Casa excluída com sucesso."})
