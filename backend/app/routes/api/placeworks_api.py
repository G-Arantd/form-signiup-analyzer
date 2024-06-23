from flask import request, jsonify
from app import app
from app.services.placeworks_services import read_placework, read_placeworks, create_placework, delete_placework, delete_all_placeworks

@app.route("/placework/<int:id>", methods=["GET"])
def placework_get(id):

    result = read_placework(id)

    if result:
        return jsonify({"sucess":True, "data": result}), 200
    else:
        return jsonify({"sucess":True, "message": "Não existe o local de trabalho informado"}), 200

@app.route("/list/placeworks", methods=["GET"])
def list_placeworks():

    result = read_placeworks()

    if result:
        return jsonify({"sucess":True, "data": result}), 200
    else:
        return jsonify({"sucess":True, "message": "Não existe Local de trabalho salvos"}), 200

@app.route("/placework", methods=["POST"])
def placework_create():

    data = request.json

    result = create_placework(data)

    return jsonify({"sucess":True, "data": result, "message": "Local de trabalho criado com sucesso"}), 200

@app.route("/placework/<int:id>", methods=["DELETE"])
def placework_delete(id):

    result = delete_placework(id)

    if result:
        message = "Local de trabalho deletado com sucesso"
    else:
        message = "Não existe local de trabalho para ser deletado"

    return jsonify({"sucess":True, "message": message}), 200

@app.route("/placeworks/delete", methods=["DELETE"])
def placeworks_all_delete():

    result = delete_all_placeworks()

    if result:
        message = "Local de trabalho deletados com sucesso"
    else:
        message = "Não existe local de trabalho para serem deletados"

    return jsonify({"sucess":True, "message": message}), 200