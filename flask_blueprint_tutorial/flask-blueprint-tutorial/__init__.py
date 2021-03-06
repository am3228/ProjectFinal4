"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment
from ddtrace import patch_all


patch_all()


def init_app():
    """Create Flask flask_sqlalchemy_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our flask_sqlalchemy_tutorial
        from .assets import compile_static_assets
        from .home import home
        from .products import products
        from .profile import profile

        # Register Blueprints
        app.register_blueprint(profile.profile_bp)
        app.register_blueprint(home.home_bp)
        app.register_blueprint(products.product_bp)

        # Compile static assets
        compile_static_assets(assets)

        return app