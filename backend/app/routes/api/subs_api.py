from flask import jsonify
from app import app

from app.services.subs_services import create_subs

@app.route("/teste")
def teste():

    teste = create_subs("C:/Users/Gabriel/Documents/GitHub/form-signiup-analyzer/csv_exemplo.csv", 1)

    return jsonify({"Teste": "Teste"})