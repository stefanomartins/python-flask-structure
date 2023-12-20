from flask import Flask
from config import Config
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.carros import bp as carros_bp
    app.register_blueprint(carros_bp, url_prefix='/carros')
    from app.casas import bp as casas_bp
    app.register_blueprint(casas_bp, url_prefix='/casas')
    from app.pessoas import bp as pessoas_bp
    app.register_blueprint(pessoas_bp, url_prefix='/pessoas')
    from flask_swagger_ui import get_swaggerui_blueprint
    swagger_ui_blueprint = get_swaggerui_blueprint(Config.SWAGGER_URL, Config.SWAGGER_API_URI, config={"app_name": "People API"})
    app.register_blueprint(swagger_ui_blueprint, url_prefix=Config.SWAGGER_URL)

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app
