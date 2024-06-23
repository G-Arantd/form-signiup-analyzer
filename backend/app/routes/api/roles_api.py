from flask import request, jsonify
from app import app
from app.services.roles_services import read_role, read_roles, create_role, delete_role, delete_all_roles

@app.route("/role/<int:id>", methods=["GET"])
def role_get(id):

    result = read_role(id)

    if result:
        return jsonify({"sucess":True, "data": result}), 200
    else:
        return jsonify({"sucess":True, "message": "Não existe o cargo informado"}), 200

@app.route("/list/roles", methods=["GET"])
def list_roles():

    result = read_roles()

    if result:
        return jsonify({"sucess":True, "data": result}), 200
    else:
        return jsonify({"sucess":True, "message": "Não existe cargos salvos"}), 200

@app.route("/role", methods=["POST"])
def role_create():

    data = request.json

    result = create_role(data)

    return jsonify({"sucess":True, "data": result, "message": "Cargo criado com sucesso"}), 200

@app.route("/role/<int:id>", methods=["DELETE"])
def role_delete(id):

    result = delete_role(id)

    if result:
        message = "Cargo deletado com sucesso"
    else:
        message = "Não existe roleo para ser deletado"

    return jsonify({"sucess":True, "message": message}), 200

@app.route("/roles/delete", methods=["DELETE"])
def roles_all_delete():

    result = delete_all_roles()

    if result:
        message = "Cargos deletados com sucesso"
    else:
        message = "Não existe cargos para serem deletados"

    return jsonify({"sucess":True, "message": message}), 200