import logging
import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    if not app.debug:
        logging.basicConfig(level=logging.INFO)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)

    from app.routes.user import user_bp
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp)

    @app.route('/')
    def index():
        selected_category = request.args.get('category', '')
        # Import here to avoid circular imports
        from app.helpers import get_products_and_categories
        products, categories = get_products_and_categories(selected_category)
        return render_template('shared/index.html', products=products, categories=categories, selected_category=selected_category)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('shared/404.html'), 404

    @login.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    return app

def init_admin_user():
    app = create_app()
    with app.app_context():
        from app.models import User
        admin_username = os.environ.get('ADMIN_USERNAME')
        admin_email = os.environ.get('ADMIN_EMAIL')
        admin_password = os.environ.get('ADMIN_PASSWORD')

        if admin_username and admin_email and admin_password:
            admin = User.query.filter_by(username=admin_username).first()
            if not admin:
                admin = User(
                    username=admin_username,
                    email=admin_email,
                    is_admin=True
                )
                admin.set_password(admin_password)
                db.session.add(admin)
                db.session.commit()
        else:
            raise ValueError("Environment variables ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD are not set.")

app = create_app()