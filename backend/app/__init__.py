from flask import Flask, json, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.models import Placeworks, Roles, Events, Subs

with app.app_context():
    db.create_all()

CORS(app)

from app.routes.test import events_test, placeworks_test, roles_test
from app.routes.api import events_api, placeworks_api, roles_api, subs_api

@app.errorhandler(ValueError)
def handle_value_error(error):
    error_message = str(error).encode('utf-8').decode('utf-8')
    response = make_response(json.dumps({"sucesso":False, "error": error_message}, ensure_ascii=False), 500)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response, 400