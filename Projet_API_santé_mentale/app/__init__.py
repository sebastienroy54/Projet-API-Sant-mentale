from flask import Flask
import sqlite3
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
from app import views
conn = sqlite3.connect("authentification.db")
print("Base de données ouverte avec succès")
conn.close()
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Pojet de questionnaires de santé mentale"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
