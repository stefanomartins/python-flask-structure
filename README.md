# python-flask-structure

Projeto de exemplo utilizando Flask, SQLAlchemy e Blueprints.

## Como executar esta aplicação?

No diretório principal digite:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

Crie a base de dados com:

```bash
flask shell
from app.extensions import db
from app.models.casa import Casa
from app.models.pessoa import Pessoa
db.create_all()
```

# Referências

- https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy