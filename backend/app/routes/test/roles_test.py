from flask import jsonify
from app import app
from app.services.roles_services import read_role, create_role, delete_role

@app.route("/roles-test", methods=["GET"])
def roles_test():

    NAMES_ERROR = ["CREATE_PLACEWORK", "READ_PLACEWORK", "DELETE_PLACEWORK"]

    error_list = []

    data_role = {"role_name": "Cargo Teste"}

    role = create_role(data_role)

    if not role:
        error_list.append(NAMES_ERROR[0])
    
    role_read = read_role(role.get("role_id"))
    
    if role_read.get("role_id") != role.get("role_id"):
        error_list.append(NAMES_ERROR[1])

    role_delete = delete_role(role.get("role_id"))

    if not role_delete:
        error_list.append(NAMES_ERROR[2])

    if error_list:
        raise ValueError({"errors": error_list})
    else:
        return jsonify({"message": "Foi realizado todos os procedimentos com sucesso"})