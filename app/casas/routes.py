from flask import request, jsonify
from app.casas import bp
from app.extensions import db
from app.models.casa import Casa


@bp.route('/', methods=['GET'])
def index():
    casas = Casa.query.all()
    data = []

    for casa in casas:
        casa_data = {
            'id': casa.id, 
            'logradouro': casa.logradouro, 
            'numero': casa.numero, 
            'complemento': casa.complemento, 
            'residentes': [{'id': pessoa.id, 'nome': pessoa.nome} for pessoa in casa.residentes]
        }
        data.append(casa_data)
    
    return jsonify(casas=data)
