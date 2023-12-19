from flask import render_template, request, jsonify
from app.people import bp
from app.extensions import db
from app.models.person import Person


@bp.route("/", methods=["GET"])
def index():
    people = Person.query.all()
    people = [person.to_dict() for person in people]
    return jsonify(people=people)


@bp.route("/<int:id>", methods=["GET"])
def show(id: int):
    person = Person.query.get(id)
    person = {"id": person.id, "name": person.name}
    return jsonify(person)


@bp.route("/add", methods=["POST"])
def create():
    if request.is_json:
        json_data = request.get_json()
        name = json_data.get("name")
        person = Person(name=name)
        db.session.add(person)
        db.session.commit()
        return jsonify({"message": "Pessoa adicionada com sucesso."})


@bp.route("/delete/<int:id>", methods=["DELETE"])
def delete(id: int):
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({"message": "Pessoa excluída com sucesso."})


@bp.route("/edit/<int:id>", methods=["PUT"])
def edit(id: int):
    if request.is_json:
        json_data = request.get_json()
        person = Person.query.get(id)
        person.name = json_data.get("name")
        db.session.commit()
        return jsonify({"message": "Pessoa atualizada com sucesso."})
